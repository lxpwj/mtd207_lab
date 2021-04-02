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
imF = dct2(img_gray)
im_reconstructed = idct2(imF)

# plot original and reconstructed images with matplotlib.pylab
plt.gray()
plt.subplot(121)
plt.imshow(img_gray)
plt.title('original image')
plt.subplot(122)
plt.imshow(im_reconstructed)
plt.title('reconstructed image (DCT+IDCT)')
plt.show()

#compare the pixel value side by side
h, v = 10, 10
orig_pix = img_gray[h, v]
recon_pix = im_reconstructed[h, v]
print(f"pos {h},{v} orig:{orig_pix}, reconstructed:{recon_pix}")

# Question 1:
# think about how to do DCT in a 8x8 block level
# here is how to index an element in numpy
# https://numpy.org/doc/stable/user/basics.indexing.html

# Solution:
'''
img_size = img_gray.shape
# for forward 2d DCT on 8x8 block
dct_8x8 = np.zeros(img_size)
for i in np.r_[:img_size[0]:8]:
    for j in np.r_[:img_size[1]:8]:
        # Apply DCT to the image every 8x8 block of it.
        dct_8x8[i:(i+8), j:(j+8)] = dct(img_gray[i:(i+8), j:(j+8)])

# now inverse 2d DCT on 8x8 block
dct_8x8_reconstructed = np.zeros(img_size)
for i in np.r_[:img_size[0]:8]:
    for j in np.r_[:img_size[1]:8]:
        # Apply inverse DCT to the DCT results every 8x8 block of it.
        dct_8x8_reconstructed[i:(i+8), j:(j+8)
                              ] = idct(dct_8x8[i:(i+8), j:(j+8)])
plt.gray()
plt.subplot(131)
plt.imshow(img_gray)
plt.title('original image')
plt.subplot(132)
plt.imshow(dct_8x8_reconstructed)
plt.title('reconstructed image (DCT+IDCT) 8x8 block')
plt.subplot(133)
plt.imshow(im_reconstructed)
plt.title('reconstructed image (DCT+IDCT)')
plt.show()
'''
