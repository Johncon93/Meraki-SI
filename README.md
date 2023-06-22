## Description

This is a basic script to run a series of GET requests to the Meraki dashboard API and retrieve L3 switch info. Retrieved information is parsed and stored in corresponding csv files and a single txt file containing a full account in JSON

## Dependencies
<b>The script requires the following dependencies:
* Python3  version 3.7 or above - https://www.python.org/downloads/
 * Python Meraki SDK - https://pypi.org/project/meraki/
	-	Install Meraki SDK via CMD prompt
		> py -m pip install meraki
* Valid Meraki API key - https://documentation.meraki.com/General_Administration/Other_Topics/Cisco_Meraki_Dashboard_API

<b>The script targets the serial No. of a L3 switch and the following must be true for the script to work:
* Switch must be allocated to a network within an organisation that has API access enabled
* The switch must have L3 configuration settings or else the script will return an empty dictionary

## Installation

<b>Ensure dependencies Python3 and the Python Meraki SDK are installed then proceed with the below. 
1. Clone the repository using GIT or download the ZIP file

	![Download options](https://i.imgur.com/6WBEet5.png "Download options")
2. Extract the ZIP contents and navigate to the folder via CMD prompt

	![CMD Prompt ](https://i.imgur.com/p6klzBt.png "CMD Prompt")
3. Update the api_key variable inside the 'key.py' file with your own API key
	> api_key  =  '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

## Usage

1. Navigate to the folder via CMD prompt

2. Initiate the script using the below command and enter the target serial when prompted
	> py .\switch_info.py
	>
	>Please enter the serial No. of the target switch without any "-". E.g. Q2QN9J8LSLPD or q2qn9j8lslpd
	>_> Q2QN9J8LSLPD
3. Retrieved data from individual requests will then be saved inside a series of corresponding CSV files, and a JSON summary covering all retrieved data will be saved as a txt file.
