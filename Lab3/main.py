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


# 4. The build_xml_element function receives the following parameters: tag, content, and
# key-value elements given as name-parameters. Build and return a string that represents
# the corresponding XML element.
# Example:
# build_xml_element ("a", "Hello there", href =" http://python.org ",
# _class =" my-link ", id= " someid ") returns the string =
# "<a href="http://python.org \ "_class = " my-link \ "id = " someid \ "> Hello there "


def build_xml_element(tag, content, **kwargs):
    xml_element = "<{} ".format(tag)
    for key, value in kwargs.items():
        xml_element += "{}=\"{}\", ".format(key.strip(), value.strip())
    xml_element = xml_element[:-2]
    xml_element += ">{}</{}>".format(content, tag)
    return xml_element


# print(build_xml_element("a", "Hello there", href=" http://python.org ",
#           _class=" my-link ", id=" someid "))


# 5. The validate_dict function that receives as a parameter a set of tuples ( that
# represents validation rules for a dictionary that has strings as keys and values)
# and a dictionary. A rule is defined as follows: (key, "prefix", "middle", "suffix").
# A value is considered valid if it starts with "prefix", "middle" is inside the value
# (not at the beginning or end) and ends with "suffix". The function will return True
# if the given dictionary matches all the rules, False otherwise.
# Example:
# the rules s={("key1", "", "inside", ""), ("key2", "start", "middle", "winter")} and
# d= {"key1": "come inside, it's too cold out", "key3": "this is not valid"}
# => False because although the rules are respected for "key1" and "key2" "key3"
# that does not appear in the rules.

def validate_dict(rule_set, d):
    for key, value in d.items():
        rules = [rule for rule in rule_set if rule[0] == key]
        for rule in rules:
            if not value.startswith(rule[1]):
                return False
            if not value.endswith(rule[3]):
                return False
            if value[1:-1].find(rule[2]) < 0:
                return False
    return True


# print(validate_dict({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},
#                     d={"key1": "come inside, it's too cold out", "key3": "this is not valid"}))

# print(validate_dict({("key1", "", "inside", ""), ("key2", "start", "middle", "winter")},
#                     d={"key1": "come inside, it's too cold out"}))


# 6. Write a function that receives as a parameter a list and returns a tuple (a, b),
# representing the number of unique elements in the list, and b representing the
# number of duplicate elements in the list (use sets to achieve this objective).

def ex6(lst):
    s = set(lst)
    return tuple((len(s), len(lst) - len(s)))


# print(ex6([1, 2, 2, 3, 3]))


# 7. Write a function that receives a variable number of sets and returns a
# dictionary with the following operations from all sets two by two: reunion,
# intersection, a-b, b-a. The key will have the following form: "a op b", where a
# and b are two sets, and op is the applied operator: |, &, -.

def ex7(*sets):
    dct = {}
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            dct["{} | {}".format(sets[i], sets[j])] = sets[i] | sets[j]
            dct["{} & {}".format(sets[i], sets[j])] = sets[i] & sets[j]
            dct["{} - {}".format(sets[i], sets[j])] = sets[i] - sets[j]
            dct["{} - {}".format(sets[j], sets[i])] = sets[j] - sets[i]
    return dct


# print(ex7({1, 2}, {2, 3}, {3, 4}))


# 10. Write a function that receives a single dict parameter named mapping. This
# dictionary always contains a string key "start". Starting with the value of this
# key you must obtain a list of objects by iterating over mapping in the following
# way: the value of the current key is the key for the next value, until you find a
# loop (a key that was visited before). The function must return the list of
# objects obtained as previously described.

def ex10(mapping):
    x = mapping["start"]
    result = [x]
    while mapping[x] not in result:
        x = mapping[x]
        result.append(x)
    return result


# print(ex10({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))


# 11. Write a function that receives a variable number of positional arguments and a
# variable number of keyword arguments adn will return the number of positional
# arguments whose values can be found among keyword arguments values.

def ex11(*args, **kwargs):
    result = 0
    for arg in args:
        if arg in kwargs.values():
            result += 1
    return result


print(ex11(1, 2, 3, 4, x=1, y=2, z=3, w=5))
