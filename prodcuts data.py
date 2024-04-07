import json

import requests

try:
    data = requests.get('https://fakestoreapi.com/products/categories').json()
except Exception as e:
    print(f'Error happened\n{e}')
else:

    if data:
        with open('productS_categories.json', 'w') as file:
            json.dump(data, file)
