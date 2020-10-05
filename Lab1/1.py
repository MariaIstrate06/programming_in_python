# 1. Find The greatest common divisor of multiple numbers read from the console. #

# we're creating a list of numbers from the console input
list_of_numbers = list(map(int, input().split()))


# definition of a function that calculated the greatest common divisor between two numbers
def greatest_common_divisor(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


# we define the result as the greatest common divisor between the first two numbers, in order for us to calculate
# it for every item in the list
result = greatest_common_divisor(list_of_numbers[0], list_of_numbers[1])

# we calculate GCD for every item in the list
for i in range(2, len(list_of_numbers)):
    result = greatest_common_divisor(result, list_of_numbers[i])

print(result)
