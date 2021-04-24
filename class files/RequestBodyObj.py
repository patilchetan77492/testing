import json

class RequestBody:
    def __init__(self, filename):
        self.filename = filename
    def FindRequestBody(self):
        with open(self.filename, 'r') as f:
            request_body = json.load(f)
            if "paths" in request_body:
                data = json.dumps(request_body["paths"]["resource"]["post"]["requestBody"], indent=4)
                print(data)
            else:
                print("Key doesn't exist in JSON data")


c = RequestBody('test.json')
a = c.FindRequestBody()
