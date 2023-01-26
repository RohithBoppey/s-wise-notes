from PIL import Image, ImageDraw
import numpy as np

# image data is stored in inputImage
inputImage = Image.open('Lena.png')
print(inputImage)

# finding width and height of the image
width, height = inputImage.size
print(width, height)

# get all pixel data as list
# we need to type cast as list or else it will give as an object
pixel_list = list(inputImage.getdata())
# print(pixel_list)
# This is a list of 512 * 512 -> RGB values as list

# Converting to np array is for easy access
# pixel_list = np.array(pixel_list).reshape(width, height, 3)
pixel_list = np.array(inputImage.getdata()).reshape(width, height, 3)

# print(pixel_list)
# print(pixel_list.size, pixel_list[0].size)


# Converting Lena image to grayscale image
# code for grayscale is - L
# gray_img = inputImage.convert('L')
# gray_img.show()
# gray_img.save('Lena Gray.png')

# Manual access of each pixel
# for i in range(0, height):
#     inputImage.putpixel([i,i], (255, 255, 255))
# inputImage.show();

# Write text on an image
s = "This is Rohith"
imageDrawer = ImageDraw.Draw(inputImage)
imageDrawer.text([206, 206], s, fill='red', font = '');
inputImage.show();
