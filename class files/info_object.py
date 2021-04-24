import json


class Info:
    def __init__(self, filename):
        self.filename = filename
    def FindInfo(self):
        with open(self.filename, 'r') as f:
            d = json.load(f)
            if "info" in d:
                data = json.dumps(d["info"], indent=4)
                print(data)
            else:
                print("Key doesn't exist in JSON data")


c = Info('test.json')
a = c.FindInfo()
