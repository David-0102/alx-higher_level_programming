#!/usr/bin/python3

def uppercase(str):
    """
    outputs a string in uppercase followed by new line

    :param str The string to convert to uppercase
    """
    result = ""
    for c in str:
        if 'a' <= c <= 'z':
            result += chr(ord(c) - ord('a') + ord('A'))
        else:
            result += c
        print(result)
