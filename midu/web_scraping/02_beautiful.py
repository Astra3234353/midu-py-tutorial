from bs4 import BeautifulSoup
from urllib.parse import urlparse
import requests

url = 'https://www.apple.com/es/macbook-air/'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    links = [urlparse(url ,a.get('href')) for a in soup.find_all('a')]
    print(links)