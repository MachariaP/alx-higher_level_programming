#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    # Step 1: Get the Number of Arguments
    num_args = len(argv) - 1  # Exclude the script name

    # Step 2: Print the Number of Arguments
    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print(f"{num_args} arguments:")

    # Step 3: Print the Arguments
    for i in range(num_args):
        print(f"{i + 1}: {argv[i + 1]}")

