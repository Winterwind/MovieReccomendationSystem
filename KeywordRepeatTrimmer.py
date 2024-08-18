with open("imdb-keywords.txt", "r") as file:
    text = file.read()
    # Keyword array
    keywords = text.splitlines()

with open("imdb-keywords-2.txt", "r") as file2:
    text2 = file2.read()
    more_keywords = text2.splitlines()

with open("imdb-keywords-2.txt", "w") as file3:
    for word in more_keywords:
        if word not in keywords:
            file3.write(word + '\n')
