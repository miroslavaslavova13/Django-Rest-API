import requests

endpoint = 'http://localhost:8000/api/products/1/update'

data = {
    'title': 'new name to product',
    'price': 130.00
}

get_response = requests.put(endpoint, json=data)
print(get_response.json())