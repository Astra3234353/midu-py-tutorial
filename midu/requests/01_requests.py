import requests

url = "https://jsonplaceholder.typicode.com/posts/"
respone = requests.get(url)

print(respone.json())
