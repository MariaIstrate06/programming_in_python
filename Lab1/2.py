# 2. Write a script that calculates how many vowels are in a string.

# we get a string as an input
my_string = input()

# we use a variable to count all the vowels in a for loop
vowel_count = 0
for i in my_string:
    if i in "aeiouAEIOU":
        vowel_count += 1

print(vowel_count)
