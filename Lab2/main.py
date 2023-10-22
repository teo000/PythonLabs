#       1. Write a function to return a list of the first n numbers in the
#       Fibonacci string.
import math


def fib(n):
    fib_list = [1, 1]
    for i in range(3, n):
        fib_list.append(fib_list[i - 2] + fib_list[i - 3])
    return fib_list


#      2. Write a function that receives a list of numbers and returns a list of
#      the prime numbers found in it.


def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for d in range(3, number//2, 2):
        if number % d == 0:
            return False
    return True


def prime_numbers(numbers):
    primes = []
    for number in numbers:
        if is_prime(number):
            primes.append(number)
    return primes


#      3. Write a function that receives as parameters two lists a and b and
#      returns: (a intersected with b, a reunited with b, a - b, b - a)

def union(list1, list2):
    return list(set(list1) | set(list2))


def intersection(list1, list2):
    return list(set(list1) & set(list2))


def difference(list1, list2):
    return list(set(list1) - set(list2))


#      4. Write a function that receives as a parameters a list of musical notes
#      (strings), a list of moves (integers) and a start position (integer). The
#      function will return the song composed by going though the musical notes
#      beginning with the start position and following the moves given as
#      parameter.

def compose(notes, moves, start):
    pos = start
    song = [notes[start]]
    for move in moves:
        song.append(notes[(pos+move)//len(notes)])
    return song


print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))
