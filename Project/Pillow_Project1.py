#! python 3
# name: Pillow_Project1

# Obj : Resize the images in a 300x300 square, and adds a logo to the lower-right corner
# ---------------------------------------------------------------------------------------------------
import os
from PIL import Image

Var_Square = 300
Logo_Name = 'catlogo.png'

logoImg = Image.open(Logo_Name)
logoHeight, logoWidth = logoImg.size
logoImg2 = logoImg.resize((int(logoHeight/4),int(logoWidth/4)))
print(logoImg2.size)
testing = Image.open("Pillow.jpg")
testing.paste(logoImg2,(0,0),logoImg2)
testing.show()
# Make a folder for to store the finished images with logos
os.makedirs('Pillow_Project1_result', exist_ok=True)  # raising an exception if folder already exist , just in case!!
# Loop over all files in the working directory
for filename in os.listdir("."):
    if not (filename.endswith(".png") or filename.endswith(".jpg")) or filename == Logo_Name:
        continue
    im = Image.open(filename)
    width, height = im.size
    # Check the size of image : > 300 then need to be resized
    if width > Var_Square and height > Var_Square:
        if width > height:
            height = int((Var_Square / width) * height)
            width = Var_Square
        else:
            width = int((Var_Square / height) * width)
            height = Var_Square

        # Resize the image
        print("Resizing %s...." %(filename))
        im = im.resize((width, height))

# Loading the logo and add onto the picture
    print("Loading the logo to %s..." % (filename))
    im.paste(logoImg2,(0,0),logoImg2)
    #im.show()
# Save changes
    #print(os.getcwd())
    im.save(os.path.join('Pillow_Project1_result', filename))
