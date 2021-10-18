# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 19:52:36 2021

@author: KhoirSalam
Soal UTS Pengolahan Citra No 1	(Extended Depth of Field with mahotas Input image)
Nama : Khoirul Umam
NIM : 3332180067
"""
#=========================================================================================
import cv2
import numpy as np
import matplotlib.pylab as plt
import mahotas as mh
print(mh.__version__)

def create_image_stack(vid_file, n = 200):
    
    vidcap = cv2.VideoCapture(vid_file)
    success,image = vidcap.read()
    i = 0
    success = True
    h, w = image.shape[:2]
    imstack = np.zeros((n, h, w))
    while success and i < n:
      imstack[i,...] = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
      success,image = vidcap.read()
      i += 1
    return imstack

image = create_image_stack('sumber/highway.mp4') #cloud.mp4
stack,h,w = image.shape
plt.figure(figsize=(20,10))
plt.gray()
plt.imshow(image[0,...].astype(np.uint8)), plt.axis('off')
plt.title('Gambar Original', size=20)
plt.axis('off')
plt.show()

focus = np.array([mh.sobel(t, just_filter=True) for t in image])
best = np.argmax(focus, 0)
image = image.reshape((stack,-1)) # image is now (stack, nr_pixels)
image = image.transpose() # image is now (nr_pixels, stack)
final = image[np.arange(len(image)), best.ravel()] # Select the right pixel at each location
final = final.reshape((h,w)) # reshape to get final result
plt.figure(figsize=(20,10))
plt.imshow(final.astype(np.uint8))
plt.axis('off'), plt.title('GambarHasil.png', size=20)
plt.show()
cv2.imwrite('sumber/KeluaranNo1UTS.png', final)