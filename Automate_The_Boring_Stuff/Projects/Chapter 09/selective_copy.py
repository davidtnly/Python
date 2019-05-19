#! python3
# selective copy.py

"""
Write a program that walks through a folder tree and searches for files with a certain file extension.
 Copy these files from whatever location they are in to a new folder.
"""

import os
import re
import shutil

# This is actually a useful program that I have used numerous time. With that being said, I wanted
# to make it a bit more polished. I started off with an entry statement explaining what the program does.

print('This program is designed to pull all user-specified files from a single extension\n'
'from one directory (including the directories within) into a new folder.\n\n')