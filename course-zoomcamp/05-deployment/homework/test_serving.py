import requests
import json

customer1 = {
    "contract": "two_year",
    "tenure": 1,
    "monthlycharges": 10
}

customer2 = {
    "contract": "two_year",
    "tenure": 12,
    "monthlycharges": 10
}

url = 'http://localhost:9696/predict'
response = requests.post(url, json=customer2)
result = response.json()

print(json.dumps(result, indent=2))
