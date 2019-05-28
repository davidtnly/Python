"""
Take two lists and write a program that returns a list that contains only the elements
that are common between the two lists (without dupes).

Make sure the program works on two lists of different sizes.

Randomly generate the lists.
"""

import random

# Define new function to create the lists of randomly generated numbers
def create_list(start, end):
    num_list = []
    for i in range(start, end):
        num = random.randint(1, 100)
        num_list.append(num)
    return num_list

# Create the two lists
list_1 = create_list(1, 50)
list_2 = create_list(1, 75)

# Create an empty list to store the duplicate values
new_list = []
count = 0
for i in list_1:
    if i in list_2:
        new_list.append(i)
        count += 1

print(set(new_list))
print(len(set(new_list)))
print('\nTotal numbers added to the list: ' + str(count) + '\n')