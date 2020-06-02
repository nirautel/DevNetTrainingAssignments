import json

#Opening the json file
file_json = open('dnac_devices.json')
json_data = json.load(file_json)

#Parsing the data for the required attributes
for line in json_data['response']:
    print('Item ID :   ',line["id"])
    print('Item TYPE :   ',line["type"])
    print('Item FAMILY :   ',line["family"])
    print('Item SOFTWARE :   ',line["softwareType"])
    print('Item IP :   ',line["managementIpAddress"])
    print('\n')

#Closing Files
file_json.close()

