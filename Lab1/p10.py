def word_count(string):
    return len(string.split())


text = input("Please enter text: ")
print("Your text has", word_count(text), "words")
