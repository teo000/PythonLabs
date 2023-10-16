def extract_first_number(string):
    result = []
    for i in range(0, len(string)):
        if string[i].isdigit():
            result.append(string[i])
            i += 1
            while i < len(string) and string[i].isdigit():
                result.append(string[i])
                i += 1
            return int(''.join(result))


text = input("Enter text: ")
print(extract_first_number(text))
