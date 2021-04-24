import json

class Schema:
    def __init__(self, filename):
        self.filename = filename
    def FindSchema(self):
        with open(self.filename, 'r') as f:
            schema_data = json.load(f)
            if "components" in schema_data:
                data = json.dumps(schema_data["components"]["schemas"], indent=4)
                print(data)
            else:
                print("Key doesn't exist in JSON data")


c = Schema('test.json')
a = c.FindSchema()
