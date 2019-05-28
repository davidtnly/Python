"""
Write a password generator. Add in a mix of lowercase letters, uppercase letters, numbers, & symbols.
The passwords should be random, generating a new password everytime the user asks for a password.
"""

from random import randint
from random import choice
import string

# Create a dictionary of password strengths
strong_length = randint(9, 15)
medium_length = randint(5, 8)
length_dict = {'strong': randint(11, 20),
               'medium': randint(6, 10),
               'weak': ['rosebud', 'swordfish', 'klapaucius', 'qwertyiiiop', 'onepiece123', 'ranndomized']}

# Create an empty password holder and loop
password = []

while True:
    strength = input('Do you want a weak, medium, or strong password?\n')
    if strength in ('weak', 'medium', 'strong'):
        break
    print("Type either 'weak', 'medium', or 'strong'.")

# Define a new function to get randomized characters
def random_choice():
    letter = choice(string.ascii_letters)
    digit = randint(0, 9)
    punctuation = choice(string.punctuation)
    char = [letter, digit, punctuation]
    return choice(char)

# Define a password generating function
def generate_password(strength):
    # Loop through the length_dict dictionary
    for k, v in length_dict.items():
        if strength != k:
            pass
        else:
            if k == 'weak':
                return choice(v)
            else:
                # For loop
                for i in range(v):
                    x = random_choice()
                    password.append(x)
                # Return the string in a clean format
                return ''.join(str(x) for x in password)

print(generate_password(strength))