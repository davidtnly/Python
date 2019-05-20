#! python3
# downloadXkcd.py - Downloads every single XKCD comic

import requests, os, bs4

url = 'http://xkcd.com'  # starting url
os.makedirs('xkcd', exist_ok=True)  # store comics in /xkcd

# download up to 2140/ only and not all 2150 pictures
while not url.endswith('2140/'):  # looks like the final page ends like this: https://xkcd.com/1/#
    # ------Download the page.
    # Print the URL
    print('Downloading page %s...' % url)
#     # Use request module function to download it
#     res = requests.get(url)
#     # call raise_for_status() method to throw an exception and end the program if error with download
#     res.raise_for_status()
#     # create beautifulsoup obj from the text of the downloaded page
#     soup = bs4.BeautifulSoup(res.text)
#
#     # ------Find the URL of the comic image.
#     # <img> element for the comic image is inside a <div> element with the id attribute set to comic so #comic img
#     comicElem = soup.select('#comic img')
#
#     # ------Download the image.
#     if comicElem == []:
#         print('Could not find comic image.')
#     else:
#         try:
#             # get the src attribute from this <img> elemnt and pass it to requests.get() to download the image file
#             comicURL = 'http:' + comicElem[0].get('src')
#             # download the image
#             print('Downloading image %s...' % (comicURL))
#             res = requests.get(comicURL)
#             res.raise_for_status()
#         except requests.exceptions.MissingSchema:
#             # skip the comic
#             prevLink = soup.select('a[rel="prev"]')[0]
#             url = 'http://kcd.com' + prevLink.get('href')
#             continue
#
#     # ------Save the image to ./xkcd.
#     imageFile = open(os.path.join('xkcd', os.path.basename(comicURL)), 'wb')
#     for chunk in res.iter_content(100000):
#         imageFile.write(chunk)
#     imageFile.close()
#
#     # ------Get the Prev button's url.
#     prevLink = soup.select('a[rel="prev"]')[0]
#     url = 'http://xkcd.com' + prevLink.get('href')
#
# print('Done')