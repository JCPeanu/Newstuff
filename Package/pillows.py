# to retrieve information from the internet
import requests
 
# import two classes from the Python Image Library (PIL)
from PIL import Image, ImageFilter, ImageDraw, ImageFont #pip install pillow
 
# We're going to select randomly one of the images in the sample library
# https://github.com/lemire/kodakimagecollection
import random
images_numbers = ["01", "02", "03", "04", "05", "09", "10", "11", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"]
number = random.choice(images_numbers)
 
# save my_image into 'image.png'. mode: w for writing, b for binary
with open('image.png', 'wb') as my_image:
    # my_image is a downloaded image from the internet (notice that it's random from that picture book)
    my_image.write(requests.get(f'https://raw.githubusercontent.com/lemire/kodakimagecollection/master/kodim{number}.png').content)
 
# load the image
original = Image.open("image.png")
# open it in an image viewer
original.show()
 
# #IF you cannot see the image, you may try one of the following:
#
# #1. OS method
# #to see it in a Mac OS environment
# # import os
# # os.system("open image.png") #Will open in Preview.
#
# # #to see it in a Linux environment
# import os
# os.system("xdg-open image.png")
#
# # #to see it in a Windows environment
# # import os
# # os.system("powershell -c image.png")
#
# #2. The Matplotlib method
# # #the other way is using the matplotlib library as a proxy renderer
# import matplotlib.pyplot as plt
# plt.imshow(original)
# plt.show()
#
# # #apply a blur
blurred = original.filter(ImageFilter.BLUR)
blurred.show()
blurred.save("blurred.png")
#
# # other filters:
# # BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE, EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
#
# # separate rgb channels
r, g, b = original.split()
r.show()
r.save("r.png")
recolored = Image.merge("RGB", (b, g, r))
recolored.show()
recolored.save("recolored.png")
#
flipped_vertically = original.transpose(Image.FLIP_TOP_BOTTOM)
flipped_vertically.show()
#
g = g.rotate(45)
g.show()
#
# # remix channels
alien = Image.merge("RGB", (b, g, r))
alien.show()
#
# # other types of blurring
boxImage = original.filter(ImageFilter.BoxBlur(5))
boxImage.show()
gaussianImage = original.filter(ImageFilter.GaussianBlur(5))
gaussianImage.show()
#
# # cropping images
cropped = original.crop((1, 2, 300, 300))
cropped.show()
#
# # Creating a thumbnail
thumbnail = original.copy() #copy() is necessary here
thumbnail.thumbnail((200, 200))
thumbnail.show()
thumbnail.save("thumbnail.png")
#
# # coding can be useful to automatize processes
# print('Original photo size: ', original.size)
#
mosaic = Image.new('RGB', (2 * original.size[0], 2 * original.size[1]), (250, 250, 250))
# #
mosaic.paste(original, (0, 0))
mosaic.paste(blurred, (original.size[0], 0))
mosaic.paste(r, (0, original.size[1]))
mosaic.paste(recolored, (original.size[0], original.size[1]))
my_font = ImageFont.load_default()
# my_font = ImageFont.truetype('Gidole-Regular.ttf', size=17) #doesn't work on my OS
ImageDraw.Draw(mosaic).text((6, 8), "My mosaic", fill ="red", align ="center", font=my_font)

mosaic.save("mosaic.png", "PNG")
mosaic.show()