#!/usr/bin/python3
# Loop through the first digit from 0 to 9
for i in range(10):
    # Loop through the second digit from i+1 to 9 to ensure unique combinations
    for j in range(i + 1, 10):
        if i < 8 or j < 9:
            print("{:02d}, ".format(i * 10 + j), end="")
        else:
            print("{:02d}".format(i * 10 + j))
