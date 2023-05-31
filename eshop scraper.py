import requests
from bs4 import BeautifulSoup
import json

url = "https://www.nintendo.com/store/products/mario-kart-8-deluxe-switch/"
response = requests.get(url)

print(response)

BeautifulSoup(response.text)
response.text