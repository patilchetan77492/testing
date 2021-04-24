import json

class Server:
    def __init__(self, filename):
        self.filename = filename
    def FindServer(self):
        with open(self.filename, 'r') as f:
            server_data = json.load(f)
            if "server" in server_data:
                data = json.dumps(server_data["server"], indent=4)
                print(data)
            else:
                print("Key doesn't exist in JSON data")


c = Server('test.json')
a = c.FindServer()
