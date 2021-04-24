import json

class Parameters:
    def __init__(self, filename):
        self.filename = filename
    def FindParameters(self):
        with open(self.filename, 'r') as f:
            parameter_data = json.load(f)
            if "paths" in parameter_data or "components" in parameter_data:
                data1 = json.dumps(parameter_data["components"]["parameters"], indent=4)
                print(data1)
                data = json.dumps(parameter_data["paths"]["resource"]["get"]["parameters"], indent=4)
                print(data)

            else:
                print("Key doesn't exist in JSON data")


c = Parameters('test.json')
a = c.FindParameters()
