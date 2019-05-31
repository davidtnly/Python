# Write a function that takes a list of lists of strings and displays it in a
# well-organized table with each column right-justified
spam = 'spam'

# Create table
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

# Results would look like below
#   apples Alice  dogs
#  oranges   Bob  cats
# cherries Carol moose
#   banana David goose

# Find the longest string in each of the inner lists


def print_table(table):
    # Create variables to get number of columns and rows in the table
    num_of_lists = len(table)
    items_in_lists = len(table[0])
    max_length_list = []

    # Obtain the largest string of each inner list and set the initial value to 0
    # At the end of each loop, append the value to the list created above
    for l in table:
        max_length_item = 0
        for item in l:
            if len(item) > max_length_item:
                max_length_item = len(item)
        max_length_list.append(max_length_item)
    print(max_length_list)

    # Create a loop to print the results
    for row in range(items_in_lists):
        for col in range(num_of_lists):
            print(table[col][row].rjust(max_length_list[col]), end=' ')
        print()


print_table(tableData)