import cv2
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl


def log_transform(image):
    # Read an image
    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply log transformation method
    c = 255 / np.log(1 + np.max(image))
    log_image = c * (np.log(image + 1))

    # Specify the data type so that
    # float value will be converted to int
    log_image = np.array(log_image, dtype=np.uint8)
    return log_image

def bilateral(image):
    bilateral_blur = cv2.bilateralFilter(image, 15, 80, 80)
    return bilateral_blur

def canny(image):
    canny_img = cv2.Canny(image,100,200)
    return canny_img

def morphological_filter(image,kernelSize):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    return closing


# Display both images
path = "E:/PyCharm Community Edition 2021.3.1/probility/Crack-Detection/Sample_crack/crack_2500_1200.jpg"
kernelSize = (5,5)

image = cv2.imread(path)
bi_image = bilateral(image)
log_image = log_transform(bi_image)
canny_image = canny(log_image)
canny_raw = canny(image)
morph_out = morphological_filter(canny_image,kernelSize)

cv2.imshow('raw',image)
cv2.imshow('bi_image',bi_image)
cv2.imshow('log_image',log_image)
cv2.imshow('canny', canny_image)
cv2.imshow('canny_raw',canny_raw)
cv2.imshow('morph_out',morph_out)
cv2.waitKey(0)
