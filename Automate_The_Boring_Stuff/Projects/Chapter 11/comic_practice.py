#! python3
# comic_practice.py - Save comic images to folder

import requests
import os
import bs4

"""
Set directory if not in the correct file path
"""
print(os.getcwd())

"""
Set max image number allowed; I want to limit to download only a few files
"""
url_image_num = 45  # currently, the oldest file is at 39

"""
Create new directory to where you want to save your files
"""
os.makedirs("CnH_images", exist_ok=True)

"""
Wrap try/except for comics unable to download in a for loop
"""
# Begin for loop with the range of comics you want to download
for comic in range(39, url_image_num):
    # Setup try/except
    try:
        # Get URL
        url = 'http://explosm.net/comics/' + str(comic) + '/'
        print(url)

        # First request is the initial url, or the comic image
        res = requests.get(url)
        res.raise_for_status()

        # The url for the comic image is inside <img> tag with an id of 'main-comic'; use BeautifulSoup to read
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        # Match the <img> element
        match = soup.find('img', id='main-comic')

        # Get the src for the BeautifulSoup obj; create link to request again
        comic_url = 'http:' + match.get('src')

        # Request again
        res = requests.get(comic_url)
        res.raise_for_status()

        # If the request is successful, download the content
        # Loop creating a new file and add the extensions
        print('Downloading CnH' + str(comic + 1).zfill(4) + '...')

        # Set image path
        image_file = open(os.path.join('CnH_images', 'CnH' + str(comic+1).zfill(4)) + '.jpg', 'wb')

        # Loop through every file
        for chunks in res.iter_content(100000):
            image_file.write(chunks)
        image_file.close()
        comic += 1
        url_image_num -= 1
        url = 'http://explosm.net/comics/' + str(url_image_num - 1) + '/'
        print(url)

    except requests.exceptions.HTTPError:
        # If a comic cannot download, change the url comic number still
        print('Could not find comic number ' + str(url_image_num))
        url_image_num -= 1
        url = 'http://explosm.net/comics/' + str(url_image_num - 1) + '/'
        print(url)

print('Finished downloading comics...')