#!/usr/bin/env python3

import sys

def main():
    # Check the number of command-line arguments
    if len(sys.argv) != 2:
        print("none")
        return

    # The parameter passed to the program
    param = sys.argv[1]

    # Prompt the user to enter a word
    user_input = input("What was the parameter? ")

    # Compare the user input with the parameter and respond accordingly
    if user_input == param:
        print("Good job!")
    else:
        print("Nope, sorry...")

if __name__ == "__main__":
    main()