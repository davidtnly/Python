#! python3
# resizeandaddLogo.py - Resize all images in current working directory to fit

import os
from PIL import Image

# Get directory
os.getcwd()

# Get logo
square_fit_size = 300
logo_filename = 'catlogo.png'
logoImg = Image.open(logo_filename)
logoW, logoH = logoImg.size

# Loop over all files in the working directory
os.makedirs('withLogo', exist_ok=True)
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == logo_filename:
        continue  # skip non-image files and the logo file itself

    Img = Image.open(filename)
    width, height = Img.size

    # Check if image needs to be resized
    if width > square_fit_size and height > square_fit_size:

        # Calculate the new width and height to resize to
        if width > height:
            height = int((square_fit_size / width) * height)
            width = square_fit_size
        else:
            width = int((square_fit_size / height) * width)
            height = square_fit_size

        # Resize the image once the new image dimensions are correct then store it
        print('Resizing %s...' % (filename))
        Img = Img.resize((width, height))

    # Add the logo
    print('Adding logo to %s...' % (filename))
    Img.paste(logoImg, (width - logoW, height - logoH), logoImg)  # pass the third argument logoImg for transparency

    # Save changes
    Img.save(os.path.join('withLogo', filename))