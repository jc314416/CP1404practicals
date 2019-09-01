text = input("Text: ")
words = text.split(" ")

word_to_count = {}
for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1


sorted_words = list(word_to_count.keys())
sorted_words.sort()

for word in sorted_words:
    print("{:{}} : {}".format(word, len(max(sorted_words, key=len)), word_to_count[word]))
    # print("{} : {}".format(word, word_to_count[word]))
