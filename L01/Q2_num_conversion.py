#import libraries
import sys
import numpy as np

# set decimal number
num = -207
print(f"input decimal number: {num}")

# y = a sin(2pift)
# convert decimal to binary
n_binary = bin(num)
# convert decimal to octal
n_octal = oct(num)
# convert decimal to hex
n_hex = hex(num)

#print all results
print(f"binary: {n_binary}")
print(f"octal: {n_octal}")
print(f"hex: {n_hex}")

# for negative, can consider use two's complement format
if num < 0:
    # specify number of bits for two's complement format
    number_of_bits = 16
    # convert decimal to two's complement format
    bin_neg = np.binary_repr(num, width=number_of_bits)
    # print result
    print(f"Two's complement format: {bin_neg}")


# Question:
# think about how to use np.binary_repr to replace the API in line 10
# refer to https://numpy.org/doc/stable/reference/generated/numpy.binary_repr.html
# https://numpy.org/doc/stable/reference/generated/numpy.base_repr.html#numpy.base_repr

# Solution:
#'''
# convert decimal to binary
n_binary = np.binary_repr(num, 16)
# convert decimal to octal
n_octal = np.base_repr(num, base=8)
# convert decimal to hex
n_hex = np.base_repr(num, base=16)

print(f"binary: {n_binary}")
print(f"octal: {n_octal}")
print(f"hex: {n_hex}")
#'''
