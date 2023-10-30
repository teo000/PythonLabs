# Write a function that receives as parameters two lists a and b and returns a list of sets containing: (a
# intersected with b, a reunited with b, a - b, b - a)
def ex1(a, b):
    def intersection(a, b):
        return set(a).intersection(set(b))

    def union(a, b):
        return set(a).union(set(b))

    def dif(a, b):
        return set(a) - set(b)

    return [intersection(a, b), union(a, b), dif(a, b), dif(b, a)]


# print(ex1([4, 3, 5, 2, 2], [2, 3, 7, 9]))


# Write a function that receives a string as a parameter and returns a dictionary
# in which the keys are the characters in the character string and the values are
# the number of occurrences of that character in the given text. Example: For string
# "Ana has apples." given as a parameter the function will return the dictionary:
# {'a': 3, 's': 2, '.': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 2, ' ': 2, 'A': 1, 'n': 1} .

def ex2(string):
    dct = {}
    for char in string:
        if char in dct:
            dct[char] += 1
        else:
            dct[char] = 1
    return dct


# print(ex2("Ana has apples."))


# Compare two dictionaries without using the operator "==" returning True or False.
# (Attention, dictionaries must be recursively covered because they can contain other
# containers, such as dictionaries, lists, sets, etc.)

def ex3(a, b):
    if type(a) != type(b):
        return False
    if isinstance(a, dict):
        if a.keys() != b.keys():
            return False
        return all(ex3(a[x], a[y]) for x, y in a)
    if isinstance(a, (list, tuple)):
        if len(a) != len(b):
            return False
        return all(ex3(a[i], b[i]) for i in range(len(a)))
    return a == b


