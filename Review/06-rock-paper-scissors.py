"""
Create a rock-paper-scissors game with 2 players. Assign the second player as a computer.
"""

from random import randint

# Create a list of possible options from the game
actions = ['Rock', 'Paper', 'Scissors']

# Assign a random play to the computer
computer = actions[randint(0,2)]

# Keep track of score
wins = 0
losses = 0
ties = 0
turns = 0

# While loop through turns
while turns < 5:
    # Set player to True
    player = input('Rock, Paper, Scissors?')
    if player == computer:
        print('Tie!')
        turns += 1
        ties += 1
    elif player == 'Rock':
        turns += 1
        if computer == 'Paper':
            print('You lose!', computer, "covers", player)
            losses += 1
        else:
            print('You win!', player, 'smashes', computer)
            wins += 1
    elif player == 'Paper':
        turns += 1
        if computer == 'Scissors':
            print('You lose!', computer, 'cuts', player)
            losses += 1
        else:
            print('You win!', player, 'covers', computer)
            wins += 1
    elif player == 'Scissors':
        turns += 1
        if computer == 'Rock':
            print('You lose!', computer, 'smashes', player)
            losses += 1
        else:
            print('You win!', player, 'cuts', computer)
            wins += 1
    else:
        print('That\'s not a valid play! Check your spelling (caps)')
        break

print('\nPlayer Stats\n' +
      'Total Wins: ' + str(wins) + '\n' +
      'Total Losses: ' + str(losses) + '\n' +
      'Total Ties: ' + str(ties) + '\n')