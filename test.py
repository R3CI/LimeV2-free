import requests
from bs4 import BeautifulSoup

url = 'https://github.com/R3CI/LimeV2-free/releases/latest'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
latest_release = soup.find('span', {'class': 'css-truncate-target'}).text

print(latest_release)
