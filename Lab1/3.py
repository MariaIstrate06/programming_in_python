# 3. Write a script that receives two strings and prints the number of occurrences of the first string in the second.

# we get 2 strings from console (we use split so we can read them both at once, being separated by space
first_string, second_string = input().split()

# we initiate a counter and go into a for loop from 0 to the length of the second string. we compare the first string
# to every possibility of a substring from the second string
count = 0
for i in range(0, len(second_string)):
    if first_string == second_string[i:len(first_string)+i]:
        count += 1

print(count)
