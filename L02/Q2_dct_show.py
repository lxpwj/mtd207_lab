# Import functions and libraries
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import dct, idct

# set image file to ../data/00.bmp
# you are free to point to any other image files
IMG_FILE = os.path.join("..", "data", "zelda.bmp")

# read image file, img is a gray scale image
img_gray = cv2.imread(IMG_FILE, cv2.IMREAD_GRAYSCALE)
print(f"Reading {IMG_FILE}, img size(width,height): {img_gray.shape}")


def dct2(a):
    # 2D dct conversion
    # convert image a from spatial domain to frequency domain
    return dct(dct(a.T, norm='ortho').T, norm='ortho')


def idct2(a):
    # 2D idct converstion
    # convert image from freuqency domain back to spatial domain
    return idct(idct(a.T, norm='ortho').T, norm='ortho')


# create a variable to hold dct coefficients
img_size = img_gray.shape
# for forward 2d DCT on 8x8 block
dct_8x8 = np.zeros(img_size)
for i in np.r_[:img_size[0]:8]:
    for j in np.r_[:img_size[1]:8]:
        # Apply DCT to the image every 8x8 block of it.
        dct_8x8[i:(i+8), j:(j+8)] = dct(img_gray[i:(i+8), j:(j+8)])

# specify a position
pos = 400
# Extract a block from image
plt.subplot(1, 2, 1)
plt.imshow(img_gray[pos:pos+8, pos:pos+8], cmap='gray')
print(f"Image data at pos {pos, pos} to {pos+8, pos+8}")
print(img_gray[pos:pos+8, pos:pos+8])
plt.title("An 8x8 Image block")

# Display the dct of that block
plt.subplot(1, 2, 2)
plt.imshow(dct_8x8[pos:pos+8, pos:pos+8], cmap='gray',
           vmax=np.max(dct_8x8)*0.01, vmin=0)
print(f"DCT coefficients at pos {pos, pos} to {pos+8, pos+8}")
print(dct_8x8[pos:pos+8, pos:pos+8])
plt.title("An 8x8 DCT block")
plt.show()


# Display entire DCT
plt.figure()
plt.imshow(dct_8x8, cmap='gray', vmax=np.max(dct_8x8)*0.01, vmin=0)
plt.title("8x8 DCTs of the image")
plt.show()


# Question 1:
# think about the other postion?
# change Pos at Line 39 to see image pixels and DCT coefficients in other block
# make sure pos+8 is less than 512 as our image size is 512
