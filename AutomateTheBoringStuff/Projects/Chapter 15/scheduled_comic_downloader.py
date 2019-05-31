#! python3
# scheduled_web_comic_downloader.py

"""
To see how most of this was written see cyanide_and_happiness.py
This will only go over the scheduling portion
"""

import requests
import os
import bs4
import time

# Check directory
os.getcwd()

"""
Setting a variable in global. If we want to run this function over and over,
we need to make sure that each time the function starts it doesn't replace our
variables with the same value. So we need to put the variables OUTSIDE the function.
add global (variable_name) right after the function. Then it's a global variable and can be used 
inside the function itself.

"""

# Define global variables
comic = 1
url_image_num = 4980

def download_comic():
    global comic
    global url_image_num
    url = 'http://explosm.net/comics/' + str(url_image_num) + '/'
    try:
        # Start request to the url
        res = requests.get(url)
        res.raise_for_status()

        # Parse soup
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        match = soup.find('img', id='main-comic')

        # Get comic url
        comic_url = 'http:' + match.get('src')

        # Request comic url
        res = requests.get(comic_url)
        res.raise_for_status()

        # Download images
        print('Downloading C&H' + str(comic).zfill(4) + '...')
        image_file = open('C&H' + str(comic).zfill(4) + '.jpg', 'wb')

        # Loop through images
        for chunk in res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()
        comic += 1
        url = 'http://explosm.net/comics/' + str(url_image_num + 1) + '/'
        print(url)
    except requests.exceptions.HTTPError:
        print('No comic was found. Will try again in 8 hours.')

    # Use time.sleep(1) in a loop in seconds
    for second in range(28800):
        time.sleep(1)

# Another loop controls the function itself. Since there are three 8-hr blocks in a day, 21 for loops will run
# for a week straight.
for hour_block in range(21):
    print('Searching for new comic')
    download_comic()