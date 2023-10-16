import math

numList = [int(x) for x in input("Enter numbers for greatest common divisor: ").split()]

gcd = numList[0]

for i in range(1, len(numList)):
    gcd = math.gcd(numList[i], gcd)

print(gcd)

