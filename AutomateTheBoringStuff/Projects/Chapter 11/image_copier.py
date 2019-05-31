#! python 3
# image_copier.py - Program to copy images from certain websites like Flickr

"""
Write a program that goes to a photo-sharing website like Flickr or Imgur, searches for a category of photos,
and then downloads all the resulting images.

You could write a program that works with any photo website that has a search feature.
"""

import requests
import os
import bs4

"""
The idea is to create a folder in a directory to store all the files that you will be downloading. The steps
you need to take is to get the URL of the website, find the tag and src of the url (to obtain image link), and then
loop through every file up to a certain number that you have selected. 
"""

# Setup env and variables
os.getcwd()  # make sure this is the directory you want your new folder to be created in
os.makedirs('finalCnH', exist_ok=True)
starting_image = 39
max_image = 45

for i in  range(starting_image, max_image):
    try:
        url = 'http://explosm.net/comics/' + str(i) + '/'  # full url for the image you want to download
        print(url)

        # Get request
        res = requests.get(url)
        res.raise_for_status()

        # Parse using BeautifulSoup
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        match = soup.find('img', id='main-comic')

        # Create new comic url now that we have the comic url
        comic_url = 'http:' + match.get('src')

        # Request from comic_url
        res = requests.get(comic_url)
        res.raise_for_status()

        # Once the above is finished, we can start downloading
        print('Downloading CnH' + str(i + 1).zfill(2) + '...')

        # Create new variable and set path where we want to save the new image file
        new_image_file = open(os.path.join('finalCnH', 'CnH' + str(i + 1).zfill(2)) + '.jpg', 'wb')

        # Loop through every file
        for chunk in res.iter_content(100000):
            new_image_file.write(chunk)
        new_image_file.close()
        i += 1
        max_image -= 1
        url = 'http://explosm.net/comics/' + str(max_image - 1) + '/'
        print(url)

    except requests.exceptions.HTTPError:
        print('Could not find comic...')
        max_image -= 1
        url = 'http://explosm.net/comics/' + str(max_image - 1) + '/'
        print(url)

print('Finished downloading... check folder')