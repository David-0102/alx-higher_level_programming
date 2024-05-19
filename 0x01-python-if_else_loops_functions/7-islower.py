#!/usr/bin/python3

#checks if a character is lowercase

def islower(c):
    #:param c: the xter to check
    #: return: True if c is lowercase, False if otherwise

    return ord('a') <= ord(c) <= ord('z')

