
def is_palindrome(number):
    return str(number) == str(number)[::-1]


n = 46964
print(is_palindrome(n))


n = 46965
print(is_palindrome(n))

