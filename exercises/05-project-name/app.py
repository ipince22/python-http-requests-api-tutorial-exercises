import requests
import json

response = requests.get("https://assets.breatheco.de/apis/fake/sample/project1.php")
obj = response.json()
print(obj["name"])