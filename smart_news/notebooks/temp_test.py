import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.settings import NEWS_API_KEY
import requests

URL = f'https://newsdata.io/api/1/news?apikey={NEWS_API_KEY}&q=Tesla'

response = requests.get(URL)

print(f'Status Code: {response.status_code}')

if response.status_code == 200:
    print(response.json())
else:
    print(f'Error: {response.text}')
