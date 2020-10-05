# 10. Write a function that counts how many words exists in a text. A text is considered to be form out of words that
# are separated by only ONE space. For example: "I have Python exam" has 4 words.

my_string = input()

count = 1
for i in range(0, len(my_string)):
    if my_string[i] == ' ' and my_string[i-1] != ' ':
        count += 1

print(count)
