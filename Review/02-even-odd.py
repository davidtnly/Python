"""
Ask the user for a number and print out a message depending on the odd/even number.
"""

# Set variable
num = int(input('Give me a number.\n'))

# If/Else through the num inputs and print out a message

if num % 4 is 0:
    print('Your number is divisible by 4.')
elif num % 2 is 0:
    print('Your number is even.')
else:
    print('Your number is odd.')
