import requests
import os
import bs4

# Set directory
print(os.getcwd())
os.chdir('C:\\Users\\David Ly\\Documents\\Programming\\Python\\Automate_The_Boring_Stuff\\Projects\\Chapter 11')

# Set max image number allowed
url_image_num = 45  # Oldest = 39
# url = 'http://explosm.net/comics/' + str(url_image_num) + '/'
# print(url)

# Make new directory
os.makedirs('cynaide_and_happiness', exist_ok=True)

# Wrap try/except for comics unable to download
for comic in range(39, url_image_num):
    try:
        # Get URL
        url = 'http://explosm.net/comics/' + str(comic) + '/'
        print(url)

        # First request is the initial url, or the comic image
        res = requests.get(url)
        res.raise_for_status()

        # The url for the comic image is inside <img> tag with an id of 'main-comic'
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        match = soup.find('img', id='main-comic')

        # Get the src for the beautifulsoup obj
        comic_url = 'http:' + match.get('src')

        # Request again
        res = requests.get(comic_url)
        res.raise_for_status()

        # If the request is successful, download the content
        # Loop creating a new file and add the extensions
        print('Downloading C&H' + str(comic + 1).zfill(4) + '...')

        # Set image path
        image_file = open(os.path.join('cynaide_and_happiness', 'C&H' + str(comic + 1).zfill(4)) + '.jpg', 'wb')

        # Loop through every file
        for chunk in res.iter_content(100000):
            image_file.write(chunk)
        image_file.close()
        comic += 1
        url_image_num -= 1
        url = 'http://explosm.net/comics/' + str(url_image_num - 1) + '/'
        print(url)

    except requests.exceptions.HTTPError:
        # If a comic cannot download, change the url comic number still
        print('Could not find comic...')
        url_image_num -= 1
        url = 'http://explosm.net/comics/' + str(url_image_num - 1) + '/'
        print(url)

print('Finished downloading comics.')
