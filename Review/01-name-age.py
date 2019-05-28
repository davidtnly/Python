"""
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them to let them know when they will turn 100 years old and give a message.
"""

# Create variables
name = input('What is your name?\n')
age = int(input('What is your age?\n'))  # Change to an int to use in a sentence
current_year = 2019
age_diff = (current_year-age) + 100
year_diff = age_diff-current_year
# print(age_diff)
# print(year_diff)

# Message
msg = 'You will turn 100 in %d, which is in %d years.\n' % (age_diff, year_diff)
print(msg)

# Loop
if year_diff > 90:
    print('You\'re really young! You got potential.')
elif year_diff > 75:
    print('Enjoy the moment and live your life!')
elif year_diff > 50:
    print('How are you? Did you enjoying the moments?')
else:
    print('Hello World! Right, %s?') % name
