"""
The following program is meant to be a simple coin toss guessing game.
The player gets two guesses (it’s an easy game). However, the program has
several bugs in it. Run through the program a few times to find the bugs
that keep the program from working correctly
This is a bit different. It's not a program that can be considered "complete"
I'll post what I did with my logging module, but yours may be different.
I tried to add comments on the parts of the code I added, but since there is no
"solution", your code will look different.
"""

import random
import logging

logging.basicConfig(level = logging.DEBUG, format = ' %(asctime)s - ''%(levelname)s - %(message)s')  # new

logging.debug('Start of program')
guess = ''

# While loop with input as heads or tails
while guess not in ('heads', 'tails'):
    logging.debug('Start of guess')  # new
    print('Guess the coin toss! Enter heads or tails: ')
guess = input()

logging.debug('Start of coin toss')  # new
toss = random.randint(0, 1)  # 0 is tails, 1 is heads

# We need to convert heads/tails to 0/1, or visa versa
if toss == 0:
    toss = 'tails'
if toss == 1:
    toss = 'heads'

logging.debug('Does ' + str(toss) + ' equal ' + str(guess) + '?')  # new

guess_num = 0
while guess_num < 5:
    if toss == guess:
        print('You got it!')
        break
    else:
        print('Nope! Guess again!')
        guess = input()
        if toss == guess:
            print('You got it!')
            break
        else:
            print('Nope. You are really bad at this game.')
            guess_num += 1