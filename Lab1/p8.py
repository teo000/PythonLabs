def no_of_ones_binary(num):
    return list(str(bin(num))).count('1')


num = int(input("Please enter a number: "))
print("Your number has", no_of_ones_binary(num), "bits with value 1!")
