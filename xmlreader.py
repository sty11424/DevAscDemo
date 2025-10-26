import xmltodict

# the 'with' statement ensures proper file handling; opening/closing when read is complete
with open('r1.xml') as file:
    xml_data = file.read() # read the entire contents of r1.xml and stored in xml_data variable

# use the parse method from xmltodict to convert XML string into a Python dictionary and store in data variable
data = xmltodict.parse(xml_data)

# print(data)

# access and print the interfaces key/section of the router dictionary, first interface IP address
print(data['router']['interfaces']['interface'][0]['ip'])
