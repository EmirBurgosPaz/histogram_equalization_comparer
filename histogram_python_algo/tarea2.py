import numpy as np
import cv2
import math

img = cv2.imread('C:/Users/NVIDIA/Desktop/vision_por_computadora/Libreria de programas/histogram_python_algo/comparator_histogram.jpg', cv2.IMREAD_GRAYSCALE)

height = img.shape[0]
width = img.shape[1]
pixels = width * height

hist, bins = np.histogram(img.flatten(), 256, [0, 256])

cdf = hist.cumsum()

for i in np.arange(height):
    for j in np.arange(width):
        a = img.item(i, j)
        b = math.floor(cdf[a] * 255 / pixels)
        img.itemset((i, j), b)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
