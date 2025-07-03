import requests

url = 'https://www.apple.com/es/macbook-air/'

response = requests.get(url)

if response.status_code == 200:
    print('Request was successful!')
    
    html = response.text