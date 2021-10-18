# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 22:30:49 2021
Soal UTS Pengolahan Citra No 6	(Steganography and Steganalysis)
Nama : Khoirul Umam
NIM : 3332180067
@author: KhoirSalam
"""

import stegano
from PIL import Image, ImageChops
from stegano import lsb, lsbset
from stegano.steganalysis import statistics, parity
import matplotlib.pylab as plt
cover = Image.open('sumber/lena.png').convert('RGB')
stego = lsb.hide("sumber/lena.png", 10*"Python Image Processing Cookbook - LSB data hiding with Stegano").convert('RGB')
stego.save("sumber/lena-secret.png")
print(lsb.reveal("sumber/lena-secret.png"))
parity_encoded_cover = parity.steganalyse(cover)
parity_encoded_stego = parity.steganalyse(stego)
_, cover_common = statistics.steganalyse(cover)
_, stego_common = statistics.steganalyse(stego)

plt.figure(figsize=(30,20))
plt.subplot(231), plt.imshow(cover), plt.axis('off'), plt.title('Gambar Sampul', size=20)
plt.subplot(232), plt.imshow(stego), plt.axis('off'), plt.title('Gambar Stegano', size=20)
plt.subplot(233), plt.imshow(ImageChops.difference(stego, cover)), plt.axis('off'), plt.title('Diff Image', size=20)
plt.subplot(234), plt.imshow(parity_encoded_cover), plt.axis('off'), plt.title('Parity Encoded Cover Image', size=20)
plt.subplot(235), plt.imshow(parity_encoded_stego), plt.axis('off'), plt.title('Parity Encoded Stego Image', size=20)
plt.subplot(236), plt.imshow(ImageChops.difference(parity_encoded_stego, parity_encoded_cover)), plt.axis('off'), plt.title('Diff in Parity Encoded Images', size=20)
plt.show()