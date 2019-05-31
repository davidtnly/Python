#! python3
# filling_the_gaps.py - find files with a prefix and find gaps between files and close the gap with new files

"""
Write a program that finds all files with a given prefix, such as spam1.txt and spam3.txt but no spam2.txt
in a single folder and locates any gaps in the numbering. Have the program rename all the later files to close the gap.

As an added challenge, write another program that can insert gaps into numbered files so that a new file can be added

A note for this program. Easier to rename all the files in the program. Renaming every file takes nearly no time
at all and it only takes a few lines

zfill() function
This function is not taught in the book but it's very simple to use and makes this program easy to run. It fills
in extra zeroes to the left to a specific width. The first step is converting your number to a string using str().
Then pass zfill() with an argument for how many zeroes you want.
"""

# 3 vs 003
foo = str(3)
print(foo)
print(foo.zfill(3))

import os
import re
import shutil

# Get directory
print(os.chdir('C:\\Users\\David Ly\\Documents\\Programming\\Python\\Automate_The_Boring_Stuff\\Projects\\Chapter 09'))
print(os.getcwd())
print(os.listdir())
path = os.getcwd()

# Create a reg expression to match the prefix you are looking for
prefix_Regex = re.compile(r'^(spam)(\d{,2})') # spam01

"""
Add an iterator to rename the end of each file
To rename, you use shutil.move(source, new path); Note: You will need the full path and not just the file name
The old name will be the absolute path to the file. This will be achieved by using os.path.abspath(filename)
The new name is trickier. You don't want to pull the file extension out so if you set up your Regex up with groups
you can pull just the word you want. In this example 'spam'
So the suffix of ONLY the filename will be the regex group, plus your iterator with zfill, and then you need to
add the file extension back so the file is usable. In this example it's '.txt'. Save this to a new variable
For full name you need to combine the absolute path with the path of the folder + the new variable created.
Then it's easy to call shutil.move(source, new name) to rename all the files.
"""

i = 1
# Loop through directory list
for file in os.listdir('.'):
    mo = prefix_Regex.search(file)
    # If true then get the absolute file path and convert it with the new file name
    if mo:
        old_name = os.path.abspath(file)
        # mo.group(1) suffix will be 'spam' + str(number value).zfill(1) + file type extension
        new_suffix = mo.group(1) + str(i).zfill(1) + '.txt'
        # Update the file names to the new file names with the suffix
        new_name = os.path.join(path, new_suffix)
        i += 1
        print('Renaming: %s to %s' % (old_name, new_name))
        shutil.move(old_name, new_name)

"""
Renaming: ..Projects\Chapter 09\spam.txt          to ..Projects\Chapter 09\spam1.txt
Renaming: ..Projects\Chapter 09\spam01.txt        to ..Projects\Chapter 09\spam2.txt
Renaming: ..Projects\Chapter 09\spam05 - Copy.txt to ..Projects\Chapter 09\spam3.txt
Renaming: ..Projects\Chapter 09\spam07.txt        to ..Projects\Chapter 09\spam4.txt
"""