import requests

base_url = "https://petstore.swagger.io/v2"

def get_request(endpoint, params=None, headers=None):
    url = f"{base_url}/{endpoint}"
    response = requests.get(url, params=params, headers=headers)
    return response

def post_request(endpoint, data=None, json=None, headers=None):
    url = f"{base_url}/{endpoint}"
    response = requests.post(url, data=data, json=json, headers=headers)
    return response

def put_request(endpoint, data=None, json=None, headers=None):
    url = f"{base_url}/{endpoint}"
    response = requests.put(url, data=data, json=json, headers=headers)
    return response

def delete_request(endpoint, params=None, headers=None):
    url = f"{base_url}/{endpoint}"
    response = requests.delete(url, params=params, headers=headers)
    return response