#! python
# delete_unneeded_files.py - walks through a directory and finds large files

"""
Write a program that walks through a folder tree -
searches for exceptionally large files or folders, ones over 100MB -
(Remember to get the file's size by using os.path.getsize() from the os module.)
Print these files with their absolute path to the screen

Note: This program does not delete the files. Just prints them onto a screen. You can edit your program
to delete them with send2trash, but you don't want to accidentally delete a bunch of files you prefer to keep.
"""

import os
import send2trash # move unneeded files to trash

# Get current wd, move to directory if needed
os.getcwd()

# Adding an user input for the directory is beneficial since you don't have to update the code itself
# Wrap everything in a try and except statement to allow the user to type in the directory again
while True:
    try:
        dir_search = input('Please type in the path of the directory to search:\n')
        # Get directory
        os.chdir(dir_search)
        # Get absolute path
        dir_search = os.path.abspath('')
        print('Searching ' + dir_search + '...')
        # Break once finished
        break
    # Error name
    except FileNotFoundError:
        print('Path not found. Please enter a complete path.')

# 1. Search folder and sub folders and print out filters greater than 100MB
# 2. Create a full path to the filename by joining the folder_name (first argument for os.walk())
#    with the filename itself. Then you can print out the absolute path to it IF it's greater than the search size
# 3. os.path.join() is a useful function that will be used. It joins two paths together and create a new variable

""" Sample Code
for folderName, subfolders, filenames in os.walk('C:\\desired_location_folder'):
    # Start at the main folder
    print('The current folder is ' + folderName)

    # Loop through subfolders
    for subfolder in subfolders:
        print('Subfolder of ' + folderName + ': ' + subfolder)

    # Loop through all files
    for filename in filenames:
        print('File inside ' + folderName + ': ' + filename)

    print('')
"""

# Loop through folder, sub folder, and file names
filecount = 0
for folderName, subFolders, fileNames in os.walk('.'):
    for filename in fileNames:
        filename = os.path.join(folderName, filename)
        size = os.path.getsize(filename)
        if size > 1:
            print(os.path.abspath(filename) + ' - ' + str(size))
            filecount += 1

print('Total files: ' + str(filecount) + '\n')

print('Finished Running.')

"""
Listed all the files that matched the criteria; we can create the second part of this script to act on these files

Future project practice ideas: remove files, update file names, copy files to another folder
"""