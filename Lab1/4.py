# 4. Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.

input_string = input()


def upper_to_lower(my_string):
    result = [my_string[0].lower()]
    for char in my_string[1:]:
        if char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            result.append('_')
            result.append(char.lower())
        else:
            result.append(char)
    return ''.join(result)


print(upper_to_lower(input_string))
