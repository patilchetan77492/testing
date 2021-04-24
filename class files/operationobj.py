import json

class Operation:
    def __init__(self, filename):
        self.filename = filename
    def FindOperation(self):
        with open(self.filename, 'r') as f:
            operation_data = json.load(f)
            if "paths" in operation_data:
                data = json.dumps(operation_data["paths"]["resource"], indent=4)
                print(data)
            else:
                print("Key doesn't exist in JSON data")


c = Operation('test.json')
a = c.FindOperation()
