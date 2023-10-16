upperCaseString = input("Enter a string in UpperCamelCase: ")

lowerCaseString = upperCaseString[0].lower()

for c in upperCaseString[1:]:
    if c.isupper():
        lowerCaseString += "_" + c.lower()
    else:
        lowerCaseString += c

print("The string in lowercase_with_underscores: ", lowerCaseString)