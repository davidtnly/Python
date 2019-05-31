# Write a function that takes a list of lists of strings and displays it in a
# well-organized table with each column right-justified
spam = 'spam'

# Create table
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

print(len(tableData))

# Results would look like below
#   apples Alice  dogs
#  oranges   Bob  cats
# cherries Carol moose
#   banana David goose


def print_table(table):
    # Create a new list of 3 "0" values: One for each list in table Data
    col_width = 0 * len(table)

    # Search for the longest string in each list of the table data and put the numbers of char in the new list
    for y in range(len(table)):
        for x in table[y]:
            if col_width[y] < len(x):
                col_width[y] = len(x)

    # New loop and print list of lists
    for x in range(len(table[0])):
        for y in range(len(table)):
            print(table[y][x].rjust(col_width[y]), end=' ')
        print()
        x += 1


printTable(tableData)

