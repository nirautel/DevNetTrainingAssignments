import re
import json
import yaml
import xml.etree.ElementTree as ET



print('\nJSON FILES***********\n')

file_json = open('data/db.json')
data_json = json.load(file_json)
for item in data_json:
    for child in data_json[item]:
        print(item ,child + " " + str(data_json[item][child]))


print('\nXML FILES***********\n')

file_xml = open('data/db.xml')
tree = ET.parse('data/db.xml')
root = tree.getroot()
for child in root:
  for sub in child:
      print(child.tag,sub.tag,sub.text)

print('\nYAML FILES***********\n')

file_yml=open('data/db.yml')
data_yml = yaml.load(file_yml, Loader=yaml.FullLoader)
for item in data_yml:
    for child in data_yml[item]:
        print(item ,child + " " + str(data_yml[item][child]))



file_json.close()
file_xml.close()
file_yml.close()
