import requests
import json

response = requests.get("https://assets.breatheco.de/apis/fake/sample/time.php")
obj = json.loads(response.text)

print("Hora actual: "+obj["hours"] +" hrs "+obj["minutes"]+" min "+obj["seconds"]+" sec")