#!/usr/bin/python3
def print_last_digit(number):
    # Get the last digit using modulus and abs() for negative numbers
    last_digit = abs(number) % 10
    # Print the last digit without a newline after it
    print("{}".format(last_digit), end="")
    # Return the last digit
    return last_digit

