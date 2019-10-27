import wikipedia

phrase = input("Enter a title or search phrase: ")
while phrase != "":
    try:
        summary = wikipedia.summary(phrase)
        page = wikipedia.page(phrase)
        print(page.title)
        print(summary)
        print(page.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
        # index = int(input("Choose title option: "))
        # summary = wikipedia.summary(e[index])

    phrase = input("Enter a title or search phrase: ")
