# 8. Write a function that counts how many bits with value 1 a number has. For example for number 24, the binary format
# is 00011000, meaning 2 bits with value "1"

my_string = input()

number = int(my_string)
count = 0
while number != 0:
    if number % 2 == 1:
        count += 1
    number = number // 2

print(count)
