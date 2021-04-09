import requests
import json

response = requests.get("https://assets.breatheco.de/apis/fake/sample/project_list.php")
obj = response.json()
print(obj[1]["name"])