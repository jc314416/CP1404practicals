import wikipedia

search_term = input("Enter a title or search phrase: ")
while search_term != "":
    try:
        summary = wikipedia.summary(search_term)
        page = wikipedia.page(search_term)
        print(page.title)
        print(summary)
        print(page.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
        # index = int(input("Choose title option: "))
        # summary = wikipedia.summary(e[index])

    search_term = input("Enter a title or search phrase: ")
