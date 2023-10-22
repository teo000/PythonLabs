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
    for d in range(3, number // 2, 2):
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
        pos = (pos + move) % len(notes)
        song.append(notes[pos])
    return song


# print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))

# 5. Write a function that receives as parameter a matrix and will return the matrix obtained by replacing all the
# elements under the main diagonal with 0 (zero).

def zero_on_main_diag(matrix):
    for i in range(0, len(matrix)):
        matrix[i][i] = 0
    return matrix


# print(zero_on_main_diag([[2, 3, 6], [6, 8, 13], [5, 7, 8]]))

# 6. Write a function that receives as a parameter a variable number of lists and a whole number x. Return a list
# containing the items that appear exactly x times in the incoming lists.

def count_in_lists(*lists, count):
    big_list = []
    result = set()
    for lst in lists:
        big_list = big_list + lst
    for element in big_list:
        if element not in result and big_list.count(element) == count:
            result.add(element)
    return result


# print(count_in_lists([1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"], count=2))

#      7. Write a function that receives as parameter a list of numbers (integers) and will return a tuple with 2
#      elements. The first element of the tuple will be the number of palindrome numbers found in the list and the
#      second element will be the greatest palindrome number.

def is_palindrome(number):
    return str(number) == str(number)[::-1]


def palindrome_count_max(numbers):
    palindrome_list = []
    max_palindrome = -1
    for number in numbers:
        if is_palindrome(number):
            palindrome_list.append(number)
            if number > max_palindrome:
                max_palindrome = number
    if max_palindrome == -1:
        return tuple(([], None))
    return tuple((palindrome_list, max_palindrome))


# print(palindrome_count_max([343, 5432, 78987, 4444, 56665]))
# print(palindrome_count_max([42341, 432142, 6543]))


#       8. Write a function that receives a number x, default value equal to 1, a list of strings, and a boolean flag
#       set to True. For each string, generate a list containing the characters that have the ASCII code divisible by
#       x if the flag is set to True, otherwise it should contain characters that have the ASCII code not divisible by
#       x.

def ascii_div_x(x=1, strings=None, flag=True):
    if strings is None:
        return [[]]

    result = []
    for string in strings:
        new_list = []
        for char in string:
            if (ord(char) % x == 0) == flag and char not in new_list:
                new_list.append(char)
        result.append(new_list)
    return result


# print(ascii_div_x(2, ["test", "hello", "lab002"], False))


