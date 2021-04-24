import json
from json import JSONEncoder

class Info:
    def __init__(self, title, description, termsOfService, contact, license, version):
        self.title = title
        self.description = description
        self.termsOfService = termsOfService
        self.contact = contact
        self.license = license
        self.version = version


class Contact:
    def __init__(self, name, url, email):
        self.name = name
        self.url = url
        self.email = email

class License:
    def __init__(self, name, url):
        self.name = name
        self.url = url

# subclass JSONEncoder
class EmployeeEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__

license = License("Apache 2.0", "https://www.apache.org/licenses/LICENSE-2.0.html")
contact = Contact("API Support", "http://www.example.com/support", "support@example.com")

info = Info("Sample Pet Store App", "This is a sample server for a pet store.", "http://example.com/terms/", contact, license, "1.0.1")

print("Printing to check how it will look like")
print(EmployeeEncoder().encode(info))


infoJSONData = json.dumps(info, indent=4, cls=EmployeeEncoder)
print(infoJSONData)
