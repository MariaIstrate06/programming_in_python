# 0. Write a functions that determine the most common letter in a string. For example if the string
# is "an apple is not a tomato", then the most common character is "a" (4 times). Only letters
# (A-Z or a-z) are to be considered. Casing should not be considered "A" and "a" represent the same character.

my_string = input()

freq_list = {}
for i in my_string:
    if i != ' ':
        if i in freq_list:
            freq_list[i] += 1
        else:
            freq_list[i] = 1

print(freq_list)
maxim = 0
for index in freq_list:
    if freq_list[index] > maxim:
        maxim = freq_list[index]
print(maxim)
