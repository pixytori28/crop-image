#name:Victoria Inahuazo
#email:victoria.inahuazo11@myhunter.cuny.edu
#date: 03/26/24
#this program runs the hunter logo image from a png file

import matplotlib.pyplot as plt
import numpy as np

hunterF = input ("Enter image file name: ")
outF = input("Enter output file: ")

img = plt.imread(hunterF)

height = img.shape[0]
width = img.shape[1]

img2 = img[height//2:, :width//2]

plt.imsave(outF, img2)

