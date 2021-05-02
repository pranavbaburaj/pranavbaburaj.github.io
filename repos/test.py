import requests
import json

url = 'http://localhost:5000/'
headers = {
  'Content-Type': 'application/json'
}
data = json.dumps({"api_key" : "LOL"})
response = requests.request(
  'POST',
  'http://localhost:5000/',
  data=data,
  headers=headers,
)

print(response.content)