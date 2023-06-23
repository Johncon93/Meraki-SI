# Import modules
import key, meraki, json, csv
from datetime import date

# Initiate an instance of the Meraki dashboard
dashboard = meraki.DashboardAPI(key.api_key, suppress_logging = True)

# /devices/{serial}/switch/ports
def get_switch_ports(serial):
    try:
        response = dashboard.switch.getDeviceSwitchPorts(serial)
        #print(f'Switch_Ports: {response}')
    except:
        return ConnectionRefusedError
    
    return response

#  /devices/{serial}/switch/routing/staticRoutes
def get_static_routes(serial):

    try:
        response = dashboard.switch.getDeviceSwitchRoutingStaticRoutes(serial)
        #print(f'Static_Routes: {response}')
    except:
        return [{f'{ConnectionRefusedError}': 'No Static routes Configured'}]
    
    return response

#  /devices/{serial}/switch/routing/interfaces
def get_l3_interfaces(serial):

    try:
        response = dashboard.switch.getDeviceSwitchRoutingInterfaces(serial)
        #print(f'L3_Interfaces: {response}')
    except:
        return [{f'{ConnectionRefusedError}': 'No L3 Interfaces Configured'}]
    
    return response

# Write data to CSV file
def write_csv(filename, data):

    headers = list(data[0].keys())

    with open(f'{filename}.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = headers)
        writer.writeheader()
        writer.writerows(data)

# Write data to txt file
def write_txt(filename, data):

    with open(f'{filename}.txt', 'w') as file:
        file.write(json.dumps(data, indent = 4))

# GET switch info and call functions to write data to files.
def get_switch_info(serial):

    # Parse GET response and pass as an argument to write_csv function
    try:
        static_routes = get_static_routes(serial)
        if type(static_routes) != list:
            print('Error')
        else:
            # filename structured as '{Request}_{Serial}_{CurrentDate}' e.g. StaticRoutes_Q2QN9J8LSLPD_20230622.csv
            write_csv(f'StaticRoutes_{serial}_{date.today()}', static_routes)
    except Exception:
        print(f'Error: {str(Exception)}')
        static_routes = [{'Value': 'No static routes configured'}]
    
    try:
        l3_interfaces = get_l3_interfaces(serial)
        if type(l3_interfaces) != list:
            print('Error')
        else:
            write_csv(f'L3Interfaces_{serial}_{date.today()}', l3_interfaces)
    except Exception:
        print(f'Error: {str(Exception)}')
        l3_interfaces = [{'Value': 'No L3 Interfaces Configured'}]

    try:
        switch_ports = get_switch_ports(serial)
        if type(switch_ports) != list:
            print(f'Invalid response: {switch_ports}')
        else:
            write_csv(f'SwitchPorts_{serial}_{date.today()}', switch_ports)
    except Exception:
        print(f'Error: {str(Exception)}')

    # Compile all retrieved info into single object and write to txt file
    all_info = {
        'static_routes': static_routes,
        'l3_interfaces': l3_interfaces,
        'switch_ports': switch_ports
    }

    # filename structured as 'AllInfo_{Serial}_{CurrentDate}' e.g. AllInfo_Q2QN9J8LSLPD_20230622.txt
    write_txt(f'AllInfo_{serial}_{date.today()}', all_info)

def main():

    serial = input('Please enter the serial No. of the target switch without any "-".\nE.g. Q2QN9J8LSLPD or q2qn9j8lslpd\n> ')

    if len(serial) > 0 and len(serial) < 13:
        parsed_serial = (serial[:4] + '-' + serial[4:8] + '-' + serial[8:12])
        get_switch_info(parsed_serial)

    else:
        print('Invalid serial No.')
        main()

if __name__ == '__main__':
    main()