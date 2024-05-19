#!/usr/bin/python3
def islower(c):
    """
    checks if a character is lowercase

    :param c: the xter to check
    : return: True if c is lowercase, False if otherwise
    """
    return ord('a') <= ord(c) <= ord('z')
