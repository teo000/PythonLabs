str1 = input("Enter a string: ")
str2 = input("Enter another string: ")

count = 0
lastPos = str1.find(str2)

while lastPos >= 0:
    count += 1
    lastPos = str1.find(str2, lastPos+1)

print("The string \"{}\" appears in the string \"{}\" \"{}\" times".format(str2, str1, count))
