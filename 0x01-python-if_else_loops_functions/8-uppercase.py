#!/usr/bin/python3

def uppercase(str):
    """
    outputs a string in uppercase followed by new line

    :param str The string to convert to uppercase
    """
    if not isinstance(str, str):
        raise TypeError("Input must be a string")

    for char in str:
        #Convert lowercase xters to uppercase usinf ASCII difference
        if ord('a') <= ord(char) <=  ord('z'):
            new_char = chr(ord(char) - 32)
        else:
            new_char = char
        print(new_char, end='') #Print without newline
    print() #Add the newline after the loop
