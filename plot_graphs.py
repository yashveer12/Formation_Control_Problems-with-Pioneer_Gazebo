#!/usr/bin/env python3

# This code is used to plot the odom data already which is stored in a file.
# The each row there is 2 numbers which are x and y(This is how the data is stored in file) 
# File='/home/yashveer/Documents/pattern_data_multi.txt'

import matplotlib.pyplot as plt
import numpy as np

X1, Y1= [], []
for line in open('/home/yashveer/Documents/pattern_data_multi.txt', 'r'): 
    values = [float(s) for s in line.split()]
    
    X1.append(values[0])
    Y1.append(values[1])

#print("x",X)
plt.plot(X1, Y1)
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.show()