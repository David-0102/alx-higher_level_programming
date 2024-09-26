usr/bin/python3
def uppercase(str):
    for char in str:
        # Check if the character is a lowercase letter
        if 'a' <= char <= 'z':
            # Convert to uppercase by subtracting 32 from ASCII value
            upper_char = chr(ord(char) - 32)
        else:
            # If it's not a lowercase letter, keep the character as is
            upper_char = char
        # Print each character without adding a newline
        print("{}".format(upper_char), end="")
    # Print a newline at the end
    print()
