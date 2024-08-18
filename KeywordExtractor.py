import requests
from bs4 import BeautifulSoup

URL = 'https://www.imdb.com/search/keyword/?s=kw'
# URL2 = 'https://www.imdb.com/search/title/?explore=keywords'

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

try:
    response = requests.get(URL, headers=headers)
    response.raise_for_status()  # Check for HTTP errors
except requests.RequestException as e:
    print(f"Error fetching data: {e}")

soup = BeautifulSoup(response.text, "lxml")
stuff = [a.get_text() for a in soup.find_all('a')]

print(stuff)

