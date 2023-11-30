#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    # Step 1: Get the Arguments
    arguments = sys.argv[1:]

    # Step 2: Convert Arguments to Integers
    int_arguments = [int(arg) for arg in arguments]

    # Step 3: Sum the Integers
    result = sum(int_arguments)

    # Step 4: Print the Result
    print(result)
