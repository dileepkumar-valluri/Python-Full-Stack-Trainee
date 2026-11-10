str = input('Enter a string: ')


def reverse_string(str):
    rev = ''
    for ch in range(len(str)-1, -1, -1):
        rev += str[ch]
    return rev


print(reverse_string(str))
