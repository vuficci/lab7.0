def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

user_input = input("Введите строку: ")

if is_palindrome(user_input):
    print("Это палиндром.")
else:
    print("Это не палиндром.")