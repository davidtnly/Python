"""
Take a list and write a program that prints out all the elements of the list that are less than  5.
"""

# Create a list of numbers and an empty list to store the new values
a = [1, 1, 2, 3, 3.5, 4, 1.4, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12, 13]
b = []

# Loop through the list
count = 0
for i in a:
    if i < 5:
        b.append(i)
        count += 1
        print('Adding number ' + str(i) + ' to the new list.')

print('\nTotal numbers added to the list: ' + str(count) + '\n')
print(b)

