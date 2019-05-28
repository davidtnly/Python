"""
Print out an user input string backwards. An easy way to reverse a string is to walk backwards
through the string by slicing:

    string[::-1], which slices the sequence backwards 1 at a time.

"""

# Create variables and use the .join() method
string = input('Input a string.\n')
backwards_string = ''.join([string[::-1]])  # Method 1 - nonintuitive
rev_method = ''.join(reversed(string))      # Method 2 - intuitive

# If else statement
if string == backwards_string:
    print('Your string is a palindrome.\n')
    print('Your string is ' + backwards_string)
else:
    print('Your string is not a palinedrome.\n')
    print('Your word is ' + string)

# Using reversed() function
for i in reversed('racecar'):
    print(i)

"""
Using reversed() does not modify the original string (which wouldn't work anyway as strings are immutable)

The .join() method works as it merges all of the characters resulting from the reversed iteration.
"""

# A more classic approach to this is to convert the string input into a mutable list of characters
def rev_string(s):
    """ Return a reversed copy of 's' """
    chars = list(s)  # Splits the string into elements of a list
    for i in range(len(s) // 2):  # Rounds down if len = 5 so 2
        tmp = chars[i]
        chars[i] = chars[len(s) - i - 1]
        chars[len(s) - i - 1] = tmp
    return ''.join(chars)

""" Above is basically a straight port of a C algorithm and doesn't utilize Python's strengths. """