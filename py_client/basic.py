import requests

endpoint = "http://localhost:8000/"

get_response = requests.get(endpoint)  # HTTP Request

print(get_response.text)


