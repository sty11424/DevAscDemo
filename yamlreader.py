# Even after installing pyyaml, Python, under the hood, sees it as plain old YAML
import yaml

with open('r1.yml') as file:
    # better to use safe_load instead of load for security reasons
    data = yaml.safe_load(file)
    # opened the file, read it in as a file object, converted it from YAML to Python dictionary, and stored in data variable

print(data)