# JSON library is already available in Python standard library
import json

# open the r1.json file and store the whole file object as a variable named file
# with open('r1.json') as file:
#     # use the load method from json library to parse the JSON file into a Python dictionary and store in data variable
#     # once the file is read and parsed completely, it is automatically closed by the 'with' statement
#     data = json.load(file)

# variable router_json with a multi-line string containing JSON data from r1.json
router_dict = {
    "router": {
        "hostname": "R1",
        "interfaces": [
            {
                "id": "0",
                "enabled": "true",
                "name": "GigabitEthernet0/0",
                "ip": "192.168.1.254",
                "mask": "255.255.255.0"
            },
            {
                "id": "1",
                "enabled": "true",
                "name": "GigabitEthernet0/1",
                "ip": "172.16.1.2",
                "mask": "255.255.255.0"
            }
        ],
        "routing": {
            "routes": [
                {
                    "destination": "192.168.2.0",
                    "mask": "255.255.255.0",
                    "gateway": "192.168.1.253"
                },
                {
                    "destination": "0.0.0.0",
                    "mask": "0.0.0.0",
                    "gateway": "201.1.113.54"
                }
            ]
        }
    }
}


router_json = json.dumps(router_dict)
print(router_json)

# opens a new file data.json in write mode
# json.dump takes the dictionary in RAM, converts JSON format, and writes it to data.json file with an indentation of 2 spaces
with open('data.json', 'w') as file:
    json.dump(router_dict, file, indent=2)