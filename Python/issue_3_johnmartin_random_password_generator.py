# issue_3_johnmartin_random_password_generator.py
# Random Password Generator using Python's 'random' module
# This program generates a random password using letters, numbers, and symbols.

import random
import string

def generate_random_password(length):
    # All possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    
    # To randomly pick characters to form the password
    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


def main():
    print("Random Password Generator")

    try:
        # Ask the user how long the password should be
        length = int(input("Enter desired password length: "))


        # To make sure the length should not be less than or equal to 3
        if length <= 3:
            print("Error: Password length must be greater than 3.")
            return

         # Generate the password
        password = generate_random_password(length)
    
        print(f"\nYour random generated password: {password}\n")
    
    except ValueError:
        print("Error: You must enter a valid number.")
        

if __name__ == "__main__":
    main()
