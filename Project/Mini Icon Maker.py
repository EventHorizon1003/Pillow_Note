# name: Mini_Icon_Maker
# product a transparent grey text in jpg format

from PIL import Image, ImageDraw
from PIL import ImageFont
import os

# Create a blank canvas
canvas1 = Image.new("RGBA", (50, 50), "grey")
# canvas1.show()

# Pass the canvas to the blank canvas
canvas2 = ImageDraw.Draw(canvas1)

# Drawing the Diamond shape on the canvas
canvas2.line([0, 25, 25, 0, 50, 25, 25, 50, 0, 25], fill="black", width=2)
#canvas1.show()

# Put the J on the center on the canvas
Font = "C:\\Windows\\Fonts"
Font1 = ImageFont.truetype(os.path.join(Font, 'FRSCRIPT.TTF'), 33)
canvas2.text([16,2],"J", fill="black", font=Font1)
canvas1.show()

canvas1.save("Icon_J.png")