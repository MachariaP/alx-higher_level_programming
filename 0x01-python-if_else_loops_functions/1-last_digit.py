#!/usr/bin/python3

import random

# Step 1: Generate a random number
number = random.randint(-10000, 10000)

# Step 2: Get the last digit
last_digit = (number) % 10

# Step 3: Print the result
print("Last digit of", number, "is", last_digit, "and is", end=" ")

# Step 4: Check conditions and print additional information
if last_digit > 5:
    print("greater than 5")
elif last_digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
