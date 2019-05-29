#! python3
# 11-parse-portfolio.py - Extract information from portfolio website.

"""
Web scraping practice on portfolio's website.
"""

import os
import bs4
import requests

# Get URL
url = 'https://davidtnly.github.io/'
print(os.getcwd())  # Check directory, file will be saved to the Outputs Folder

"""
The requests library will make a GET request to a web server, which will download the HTML contents of a given web page.
After running our request, we get a Response object. This object has a status_code property, which 
indicates if the page was downloaded successfully. A status_code of 200 means that the page downloaded successfully.
"""
print('Accessing...' + url + '\n')
res = requests.get(url)
res.raise_for_status()

"""
We can use the BeautifulSoup library to parse this document, and extract the text from the img and href tag. 
We first have to import the library, and create an instance of the BeautifulSoup class to parse our document
"""
soup = bs4.BeautifulSoup(res.text, 'html.parser')
# print(soup.prettify())  # Print out HTML content of the page, formatted nicely

"""
Get the elements from the text
1. Print the image file names
2. Print the links to the images (projects)
"""
# Gets the <p> element paragraph text
p_len = soup.find_all("p")
print(len(p_len))

for i in range(0, len(p_len)):
    paragraphs = soup.find_all("p")[i].text
    print(paragraphs)

# Image names
imgContent = []
imgElem = soup.findAll('img')
for image in imgElem:
    print(image['src'])
    # imgElem.append(image)

# Links; Look for tags with specific class attributes
# linkElem = soup.findAll('article', class_='item')  # <article class="item">
linkElem = soup.findAll('a', class_='_blank')  # <a href="#" class="image fit">
# linkElem = soup.findAll('a', {'target':'_blank', 'href':True})['href']
# linkElem = soup.select('.blank')

print(type(linkElem))  # Returns .ResultSet object which is a list containing the divs
print(len(linkElem))

for link in linkElem:
    print(link.get('href'))

# liElem = soup.findAll('h3')
# print(liElem)
