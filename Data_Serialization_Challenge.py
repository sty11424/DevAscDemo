import xmltodict
import json

with open('yangwang.xml') as file:
    xml_data = file.read() # read the entire contents of r1.xml and stored in xml_data variable

data = xmltodict.parse(xml_data)

with open('yangwang.json', 'w') as file:
    json.dump(data, file, indent=2)
