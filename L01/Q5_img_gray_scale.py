import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

# set image file to ../data/00.bmp
# you are free to point to any other image files
IMG_FILE = os.path.join("..", "data", "city001.png")

# read image file, img is BGR
img_bgr = cv2.imread(IMG_FILE, cv2.IMREAD_COLOR)
print(f"Reading {IMG_FILE}, img size(width,height,channels): {img_bgr.shape}")

# covert BGR format to RGB format
# matplotlib support RGB format only
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

# convert image to gray scale
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
print(
    f"Gray scale image conversion done: img size(width, height):{img_gray.shape}")

# convert image from gray to black and white
# https://docs.opencv.org/4.4.0/d7/d4d/tutorial_py_thresholding.html
threshold, img_black_white = cv2.threshold(
    img_gray, 127, 255, cv2.THRESH_BINARY)
print(
    f"Black and White image conversion done: img size(width, height):{img_black_white.shape} ")
print(f"Black and White image threshold: {threshold}")


# compare image side by side
plt.subplot(1, 3, 1)
plt.imshow(img_rgb)
plt.title("Color image")
plt.subplot(1, 3, 2)
plt.imshow(img_gray, cmap='gray', vmin=0, vmax=255)
plt.title("Gray image")
plt.subplot(1, 3, 3)
plt.imshow(img_black_white, cmap='gray', vmin=0, vmax=255)
plt.title("Black&whilte image")
plt.show()


# Question 1:
# think about how to print values of a specific position of gray scale image, e.g., pos(0,0)
# here is how to index an element in numpy
# https://numpy.org/doc/stable/user/basics.indexing.html
# compare to question in Q3_4_img_read.py to see difference between color image and gray scale image

# Solution:
#'''
h = 0
v = 0
gray_val = img_gray[v, h]
print(f"Gray value:{gray_val}")
#'''


# Question 2:
# think about how to separate R Channel, G channel and B channel data?
# https://docs.opencv.org/4.4.0/d3/df2/tutorial_py_basic_ops.html
# split image into channels

# Solution:
#'''
n_b, n_g, n_r = cv2.split(img_bgr)
print(f"split image into R/G/B, size (width, height): {n_b.shape}")
#plot image for comparision
plt.subplot(1, 4, 1)
plt.imshow(img_rgb)
plt.title("Color image")
plt.subplot(1, 4, 2)
plt.imshow(n_b, cmap='Blues_r')
plt.title("Blue channel image")
plt.subplot(1, 4, 3)
plt.imshow(n_g, cmap='Greens_r')
plt.title("Green channel image")
plt.subplot(1, 4, 4)
plt.imshow(n_r, cmap='Reds_r')
plt.title("Red channel image")
plt.show()
#'''
