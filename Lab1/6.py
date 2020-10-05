# 6. Write a function that validates if a number is a palindrome.

number = input()

if number == number[::-1]:
    print('true')
else:
    print('false')