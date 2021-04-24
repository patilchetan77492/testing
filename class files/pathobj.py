import json

class Paths:
    def __init__(self, filename):
        self.filename = filename
    def FindPaths(self):
        with open(self.filename, 'r') as f:
            path_data = json.load(f)
            if "paths" in path_data:
                data = json.dumps(path_data["paths"], indent=4)
                print(data)
            else:
                print("Key doesn't exist in JSON data")


c = Paths('test.json')
a = c.FindPaths()
