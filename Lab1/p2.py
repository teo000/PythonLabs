string = input("Enter a string: ")
vowels = set("aeiouAEIOU")

count = 0

for letter in string:
    if letter in vowels:
        count = count + 1

print("The string has", count, "vowels")



