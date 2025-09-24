#imports requests and uses it to get response status code
import requests

def get_status_code(url="https://google.com/get"):
    response = requests.get(url, timeout=5)
    return response.status_code