import requests
from bs4 import BeautifulSoup
import re

# the base url that will be added to depending on what genre(s)/descriptor(s) the user selects
URL = 'https://www.imdb.com/search/title/?title_type=feature'

# Genre array
GENRES = {
    "action", "adventure", "animation", "biography", "comedy", "crime", "documentary", "drama", "family", "fantasy",
    "noir", "gameshow", "history", "horror", "music", "musical", "mystery", "news", "reality tv", "romance", "sci-fi",
    "short", "sport", "talk show", "thriller", "war", "western"
}

# Keyword array
with open("imdb-keywords.txt", "r") as file:
    text = file.read()
KEYWORDS = text.splitlines()


def scraper(url):
    # print("ok", url)
    if not url:
        print("Invalid genre.")
        return []

    headers = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for HTTP errors
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

    soup = BeautifulSoup(response.text, "lxml")

    # Extract movie titles
    titles = [a.get_text() for a in soup.find_all('a', href=re.compile(r'/title/tt\d+/'))]
    return titles


if __name__ == '__main__':
    genre_list = []
    kw_list = []
    order = ""

    while True:
        try:
            index = int(
                input('Would you like to order your recommendations based on\n1. acclaim\n2. all-time popularity\n3. '
                      'what\'s hot now\n(please respond with the number associated with the desired option)\n'))
            break
        except ValueError as e:
            print('Please enter a valid response')
            continue

    while (index != 1) and (index != 2) and (index != 3):
        print('Please enter a valid response')
        index = int(input())
    if index == 1:
        URL += '&num_votes=70000,'  # this ensures that the list won't be flooded with obscure bollywood movies
        order = '&sort=user_rating,desc'
    elif index == 2:
        order = '&sort=num_votes,desc'

    genre = str(input('Please enter as many genres/subgenres as you like; '
                      'when you\'re done, hit enter without typing anything. \n'
                      'Keep and mind that entering more genres will narrow your search further to things that contain '
                      'ALL the genres/subgenres you listed\n'))
    while genre != '':
        if genre.lower() not in GENRES:
            print('Please enter a valid genre')
            genre = str(input())
            continue
        genre_list.append(genre.lower())
        genre = str(input())

    # print(genre_list)  # for testing purposes; remove later

    if len(genre_list) > 0:
        URL += '&genres='
        for entry in range(len(genre_list)):
            URL += genre_list[entry]
            if entry != (len(genre_list) - 1):
                URL += ','

    # print(URL)

    kw = str(input('Please enter as descriptors/keywords as you like; '
                   'when you\'re done, hit enter without typing anything.\n'
                   'Keep and mind that entering more keywords will narrow your search further to things that '
                   'contain ALL the keywords you listed.\nIn addition, keywords must only contain alphanumerical '
                   'characters, so no punctuation and the like.\n'))
    while kw != '':
        if kw.lower() not in KEYWORDS:
            print('Please enter a valid keyword')
            kw = str(input())
            continue
        kw_list.append(kw.lower())
        kw = str(input())

    # print(kw_list)  # for testing purposes; remove later

    if len(kw_list) > 0:
        URL += '&keywords='
        for entry in range(len(kw_list)):
            if ' ' in kw_list[entry]:
                kw_list[entry] = kw_list[entry].replace(' ', '-')
            URL += kw_list[entry]
            if entry != (len(kw_list) - 1):
                URL += ','

    URL += order
    # print(URL)  # for testing purposes

    movie_titles = scraper(URL)
    if not movie_titles:
        print("No movies found. Try broadening your query.")
    else:
        # max_titles = 14 if genre_list in GENRES else 12
        for movie in movie_titles[:14]:
            print(movie)
#
