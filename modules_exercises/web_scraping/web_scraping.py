import requests
from bs4 import BeautifulSoup

url = "https://www.youtube.com/?&ab_channel=pythonando"
response = requests.get(url)
