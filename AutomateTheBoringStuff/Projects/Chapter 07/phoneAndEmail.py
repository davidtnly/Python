#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?     # area code
    (\s|-|\.)?             # separator
    (\d{3})                # first 3 digits
    (\s|-|\.)              # separator
    (\d{4})                # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
    )''', re.VERBOSE)

# Create email regex.
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4}){1,2} # dot-something
    )''', re.VERBOSE)

# Find all matches in the clipboard text
text = str(pyperclip.paste())
# Create empty list to store variables
matches = []

# Loop through list
for groups in phoneRegex.findall(text):
    # There is one tuple for each match, and each tuple contains strings for each group in the regular expression.
    # Remember that group 0 matches the entire regular expression, so the group at index 0 of the tuple is the one
    # you are interested in.
    # These groups are the area code, first three digits, last four digits, and extension
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Join the matches into a string for the clipboard
# Copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')

# Results - https://nostarch.com/contactus
# 800-420-7240
# 415-863-9900
# 415-863-9950
# info@nostarch.com
# media@nostarch.com
# academic@nostarch.com
# info@nostarch.com

# Testing

# Text
mo = phoneRegex.findall('800.420.7240')
print(mo) # full text
print(mo[0]) # 0th element (which is the list)
print(mo[0][0])
print(mo[0][1])
print(mo[0][3])
print(mo[0][5])
print('-'.join([mo[0][1], mo[0][3], mo[0][5]]))