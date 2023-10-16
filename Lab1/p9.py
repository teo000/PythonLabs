from string import ascii_lowercase


def most_common_letter(string):
    char_list = list(string.lower())
    max_count = 0
    result = ''
    for c in ascii_lowercase:
        curr_count = char_list.count(c)
        if max_count < curr_count:
            max_count = curr_count
            result = c

    return result


text = input("Enter text: ")
print("Most common letter is", most_common_letter(text))
