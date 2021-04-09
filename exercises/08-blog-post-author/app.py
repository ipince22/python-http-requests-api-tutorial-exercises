import requests

# your code hereimport requests
import json

response = requests.get("https://assets.breatheco.de/apis/fake/sample/weird_portfolio.php")
obj = response.json()


print(obj["posts"][0]["title"])