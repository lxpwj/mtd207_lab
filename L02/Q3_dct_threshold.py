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

# now inverse 2d DCT on 8x8 block
dct_8x8_reconstructed = np.zeros(img_size)
for i in np.r_[:img_size[0]:8]:
    for j in np.r_[:img_size[1]:8]:
        # Apply inverse DCT to the DCT results every 8x8 block of it.
        dct_8x8_reconstructed[i:(i+8), j:(j+8)
                              ] = idct(dct_8x8[i:(i+8), j:(j+8)])

# Threshold (TRY YOUR THRESHOLD!!!!)
thresh = 0.01
# discard those coefficients below threshold
dct_thresh = dct_8x8 * (abs(dct_8x8) > (thresh*np.max(dct_8x8)))
percent_nonzeros = np.sum(dct_thresh != 0.0) / (img_size[0]*img_size[1]*1.0)
print(f"Keeping only {percent_nonzeros*100.0} of the DCT coefficients")

# now inverse 2d DCT on 8x8 block for thie threashold-ed DCT coefficients
dct_8x8_reconstructed_th = np.zeros(img_size)
for i in np.r_[:img_size[0]:8]:
    for j in np.r_[:img_size[1]:8]:
        # Apply inverse DCT to the DCT results every 8x8 block of it.
        dct_8x8_reconstructed_th[i:(i+8), j:(j+8)
                                 ] = idct(dct_thresh[i:(i+8), j:(j+8)])

# specify a position
pos = 20
print(f"Image data at pos {pos, pos} to {pos+8, pos+8}")
print(img_gray[pos:pos+8, pos:pos+8])
print(f"DCT coefficients at pos {pos, pos} to {pos+8, pos+8}")
print(dct_8x8[pos:pos+8, pos:pos+8])
print(f"DCT coefficients with threshold at pos {pos, pos} to {pos+8, pos+8}")
print(dct_thresh[pos:pos+8, pos:pos+8])

plt.gray()
plt.subplot(131)
plt.imshow(img_gray)
plt.title('original image')
plt.subplot(132)
plt.imshow(dct_8x8_reconstructed)
plt.title('reconstructed image (DCT+IDCT) 8x8 block')
plt.subplot(133)
plt.imshow(dct_8x8_reconstructed_th)
plt.title('reconstructed image with threshold')
plt.show()

# Question 1:
# think about changing threshold of DCT?
# change thresh at Line 47 to see how this value affect final output
