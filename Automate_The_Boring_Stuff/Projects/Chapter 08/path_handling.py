import os
# os.path module provides functions for returning the absolute path of a relative path and for checking whether a given
# path is an absolute path

# os.path.abspath(path) will return a string of the absolute path of the argument, which is an easy way to convert
# a relative path into an absolute one
p = os.path.abspath(' .')
print(p)
os.path.abspath('.\\Scripts')

# os.path(isabs(path)) will return True if the argument is an absolute path and False if it's a relative path
os.path.isabs('.')

# os.path.relpath(path, start) will return a string of a relative path from the start part to path
os.path.isabs(os.path.abspath('.'))

# Read file in chapter 8 folder
test_path = os.path.relpath('\\Projects\\Chapter 08')
working_dir = os.getcwd()
print("test path", test_path)
print("working dir: ", working_dir)

# Open readthis.txt file in chapter 08 folder

# Get files in directory
os.getcwd() # get current wd
mainpath = 'C:\\Users\\David Ly\\Documents\\Programming\\Python\\Automate_The_Boring_Stuff\\Projects\\Chapter 08'
readthisfile = 'readthis.txt'
fullpath = os.path.join(mainpath, readthisfile)
print(os.path.join(mainpath, readthisfile))

# Open
chapterFile = open(fullpath)
print(chapterFile.read())

# Alternatively, you can use the readlines() method to get a list of string values from the file, one string for
# each line of text. For example, create a file named sonnet29.txt in the same directory as hello.txt and write
# the following text in it:
print(chapterFile.readlines())





"""
import os
import os.path
import shutil

# You find your current directory:
d = os.getcwd() #Gets the current working directory

# Change directory one up
os.chdir("..") #Go up one directory from working directory

# Get a tuple of all directories, for one directory up
o = [os.path.join(d,o) for o in os.listdir(d) if os.path.isdir(os.path.join(d,o))] # Gets all directories in the folder

# Search the tuple for the directory you want and open the file
for item in o:
    if os.path.exists(item + '\\testfile.txt'):
    file = item + '\\testfile.txt'
    
"""