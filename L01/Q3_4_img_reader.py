import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

# set image file to ../data/00.bmp
# you are free to point to any other image files (!!!TRY YOUR IMAGES HERE!!!!)
IMG_FILE = os.path.join("..", "data", "00.bmp")

# read image file, img is BGR
img_bgr = cv2.imread(IMG_FILE, cv2.IMREAD_COLOR)
print(f"Reading {IMG_FILE}, img size(width,height,channels): {img_bgr.shape}")

# covert BGR format to RGB format
# matplotlib support RGB format only
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

# show image
plt.imshow(img_rgb)
plt.show()


# Question 1:
# think about how to print RGB values of a specific position, e.g., pos(0,0)
# here is how to index an element in numpy
# https://numpy.org/doc/stable/user/basics.indexing.html

# Solution:
'''
h = 0
v = 0
R, G, B = img_rgb[v, h, :]
print(f"R:{R}, G:{G}, B:{B}")
'''


# Question 2:
# think about how to change RGB values of a specific position
# here is how to index an element in numpy
# https://numpy.org/doc/stable/user/basics.indexing.html
# https://docs.opencv.org/4.4.0/d3/df2/tutorial_py_basic_ops.html

# Solution:
'''
# specify location, where are modified
h_start, h_end = 100, 150
v_start, v_end = 100, 150
# copy orignal image to another place
img_rgb_changed = np.copy(img_rgb)
# change the pixels at speicified location to black color
img_rgb_changed[v_start:v_end, h_start:h_end, :] = 0
# compare image side by side
plt.subplot(1, 2, 1)
plt.imshow(img_rgb)
plt.title("original image")
plt.subplot(1, 2, 2)
plt.imshow(img_rgb_changed)
plt.title("modified image")
plt.show()
'''
