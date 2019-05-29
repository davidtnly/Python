"""
Write a program that takes a list and returns a new list that contains
the elements of the first list minus all the duplicates.
"""

# Create a color list
colors = ['red', 'red', 'purple', 'blue', 'red', 'purple', 'yellow', 'blue', 'orange']

# Create the function to remove duplicates
def remove_duplicates(list):
    new_list = []
    for i in list:
        if i in new_list:
            continue
        else:
            new_list.append(i)
    return new_list


print(remove_duplicates(colors))

# Create another function using set()
def remove_dupes(list):
    new_list = set(list)
    return new_list

print(remove_dupes(colors))