#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start of each line of text on the clipboard

# You must have copied something to the clipboard first before running the script
# Script will paste text from clipboard and do string manipulation on the pasted text
# Copy the new text to the clipboard (paste the new values somewhere)

import pyperclip

# Sample text
sample_text = 'Lists of animals\nLists of aquarium life\nLists of biologists by author abbreviation\nLists of cultivars'

# Return all the text on the clipboard as one big string
text = pyperclip.paste()  # paste text

# Separate lines and add stars
lines = text.split('\n')

# Loop through all indexes in the "lines" list, which is the text
for i in range(len(lines)):
    # Add the new '* ' text with the original text
    lines[i] = '* ' + lines[i]

# Join back the "lines" list
text = '\n'.join(text)  # with '\n' it will separate each text with a new line like the original

# Copy the new text then run the code
pyperclip.copy(text)
