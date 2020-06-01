import re
import json
import yaml
import xml.etree.ElementTree as ET


file_json = open('data/dnac_devices.json')
json_data = json.load(file_json)

#print(json_data)


for item in json_data:
    for child in json_data[item]:
        print("Device_Name---"+str(child["type"]))
        print("ID---" + str(child["id"]))
        print("family---" + str(child["family"]))
        print("SOFTWARE---" + str(child["softwareType"]))
        print("IP---" + str(child["managementIpAddress"]))




file_json.close()

