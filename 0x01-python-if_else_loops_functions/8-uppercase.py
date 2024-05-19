#!/usr/bin/python3

def uppercase(str):
    """
    Print a string in uppercase followed by new line

    :param str The string to convert to uppercase
    """
    result = ""
    for c in str:
        if 'a' <= c <= 'z':
            c = chr(ord(c) - ord('a') + ord('A'))
            result += c
            print(result)
