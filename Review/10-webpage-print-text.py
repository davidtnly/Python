"""
Using requests and BeautifulSoup, print to the screen the full text of the article on this website:

http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture


The article is long, so it is split up between 4 pages. Your task is to print out the text to the screen
so that you can read the full article without having to click any buttons.

Print it out to a .txt file.
"""

import bs4
import requests
import textwrap
import os

# Get url
url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'

# Parse the webpage
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Define a function to get text
def print_text(elem):
    for i in range(len(elem)):
        text = textwrap.wrap(elem[i].getText(), width = 80)
        for line in text:
            print(line)

"""
Use .findAll method to find multiple elements

find_all() method returns a collection of elements
"""
intro_elem = soup.findAll('div', class_='dek')
content_elem = soup.findAll('section', class_='content-section')

print_text(intro_elem[0:100])
print_text(content_elem[0:100])

# Write the text to a file
input_filename = input('What do you want the file name to be?\n')
script_num = '10-'
filename = script_num + input_filename + '.txt'

# Loop and save text into a new file to Outputs folder
open_file = open(os.path.join('Outputs', filename), 'wb')
for chunk in res.iter_content(100000):
    open_file.write(chunk)
open_file.close()

print('Parsed text to file.')
