"""
Generate a random number between 1 - 9 including (1 & 9) then ask the user to guess
the number. Tell them whether they guessed the too low or too high.

Keep the game going until the user types "exit" and keep track of the number of guesses.
"""

from random import randint

# Create random number
random_number = randint(1, 9)
print('Guess the random number.\n')

# Create counts
count = 0
guess = 0

# Create a while loop for the game
while guess is not '' and guess is not random_number:
    guess = input()
    if guess == '':
        break
    else:
        guess = int(guess)
    if int(guess) > random_number:
        print('Guess is too high. Guess again or press enter to quit.\n')
        count += 1
    elif int(guess) < random_number:
        print('Guess is too low. Guess again or press enter to quit.\n')
        count += 1
    else:
        print('You got it! It took you ' + str(count) + ' tries!')

if guess is '':
    print('You gave up!')