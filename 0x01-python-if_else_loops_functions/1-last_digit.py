#!/usr/bin/python3
import random

# Generate a random number between -10,000 and 10,000
number = random.randint(-10000, 10000)

# Determine the last digit of the number
last_digit = number % 10 * (1 if number > 0 else -1)

# Print the result
print("Last digit of", number, "is", last_digit, "and is ", end="")

# Check the conditions and print the result
if last_digit > 5:
    print("greater than 5")
elif last_digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
