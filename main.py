import json

import requests
from bs4 import BeautifulSoup


url = 'https://flagsapi.com/#countries'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

countries = []
countries_arr = []

for row in soup.find_all('div', class_='item_country'):
    code = row.find('p', class_='mb0').text.strip()
    country = row.find('p', class_='').text.strip()
    countries_arr.append(country)
    countries.append({'code': code, 'country': country, 'url': 'https://flagsapi.com/' + code + '/' + 'shiny/64.png'})

with open("countries.json", "w") as f:
    json.dump(countries, f, indent=4)

with open("countries.txt", "w") as f:
    f.write("\n".join(countries_arr))

print("Data saved to countries.json and countries.text")