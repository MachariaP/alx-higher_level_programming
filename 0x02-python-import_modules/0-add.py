#!/usr/bin/python3

# If the script is executed as the main program
if __name__ == "__main__":
    # Import the add function from the add_0 module
    from add_0 import add

    # Assign values to variables a and b
    a = 1
    b = 2

    # Print the result of the addition using the add function
    print("{} + {} = {}".format(a, b, add(a, b)))
