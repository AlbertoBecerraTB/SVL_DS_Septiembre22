import requests

url = "http://127.0.0.1:5000/store"

data = {"name": "MyStore"}

req = requests.post(url, json=data)

print(req.json())