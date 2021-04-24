import json

class Components:
    def __init__(self, filename):
        self.filename = filename
    def FindComponents(self):
        with open(self.filename, 'r') as f:
            components_data = json.load(f)
            if "components" in components_data:
                data = json.dumps(components_data["components"], indent=4)
                print(data)
            else:
                print("Key doesn't exist in JSON data")


c = Components('test.json')
a = c.FindComponents()
