from imdb import Cinemagoer, IMDbError

with open("imdb-keywords.txt", "r") as file:
    text = file.read()
    # Keyword array
    KEYWORDS = text.splitlines()

ia = Cinemagoer()

with open("imdb-keywords.txt", "w") as file:
    for word in KEYWORDS:
        print(word)
        file.write(word + '\n')
        search = ia.search_keyword(word)
        for element in search:
            if element not in KEYWORDS:
                file.write(element + '\n')

print(KEYWORDS)
