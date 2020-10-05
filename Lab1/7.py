# Write a function that extract a number from a text (for example if the text is "An apple is 123 USD", this function
# will # return 123, or if the text is "abc123abc" the function will extract 123). The function will extract only
# the first number that is found.

my_string = input()
i = 0
found_the_first = 0
new_string = []
while found_the_first != 2 and i < len(my_string):
    if found_the_first == 1 and my_string[i] not in "0123456789":
        found_the_first = 2
    if my_string[i] in "0123456789":
        new_string.append(my_string[i])
        found_the_first = 1
    i += 1
if found_the_first == 0:
    print('Not Found')
else:
    print (''.join(new_string))

