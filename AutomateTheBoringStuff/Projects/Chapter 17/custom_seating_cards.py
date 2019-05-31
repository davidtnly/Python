#! python3
# custom_seating_cards.py - Creates custom seating invitations

"""
Chapter 13 included a practice project to create custom invitations from
a list of guests in a plaintext file. As an additional project, use the
pillow module to create images for custom seating cards for your guests.
For each of the guests listed in the guests.txt file from the resources
at http://nostarch.com/automatestuff/, generate an image file with the
guest name and some flowery decoration. A public domain flower image is
available in the resources at http://nostarch.com/automatestuff/.

To ensure that each seating card is the same size, add a black rectangle
on the edges of the invitation image so that when the image is printed out,
there will be a guideline for cutting. The PNG files that Pillow produces
are set to 72 pixels per inch, so a 4×5-inch card would require a
288×360-pixel image.
"""

import os
from PIL import ImageDraw
from PIL import Image
from PIL import ImageFont

os.makedirs('seating_invitations', exist_ok=True)

# Obtain guest names from the text tile
names = open('guests.txt')
names = names.read()
names = names.split('\n')

"""
 - Create image objects and obtain their sizes in variables
 - Easier to read to use the multiple assignment method for each picture width and height
 - Resize the image to fit on the card will be dependent on the image file
"""
deathly_hallows = Image.open('deathly_hallows.jpg')
width, height = deathly_hallows.size
deathly_hallows = deathly_hallows.resize((int(width / 2.2), int(height / 2.2)))

# Open another image
owl = Image.open('owl.png')
owidth, oheight = owl.size
owl = owl.resize((int(owidth / 7), int(oheight / 7)))

# Create font folder with a font to use for the name
fonts_folder = 'C:\Windows\Fonts'
thefont = ImageFont.truetype(os.path.join(fonts_folder, 'chiller.ttf'), 50)

# Loop through all images and texts onto a design
for name in names:
    # Create a blank image
    new_image = Image.new('RGBA', (400, 320), 'white')
    newW, newH = new_image.size

    # Paste the pictures you want onto your card
    new_image.paste(deathly_hallows, (60, 20))
    new_image.paste(owl, (270, 10))

    # Draw
    draw = ImageDraw.Draw(new_image)
    draw.rectangle((4, 4, 396, 316), outline='black')
    nwidth, nheight = draw.textsize(name)
    draw.text(((400 - nwidth)/2 - 20, 150), name, fill='aliceblue', font=thefont)

    # Save
    new_image.save(os.path.join('seating_invitations', name + '_Invite.png'))