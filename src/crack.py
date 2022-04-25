import cv2
from PIL import Image
import os

def crop(path, input, height, width):
    im = Image.open(input)
    imgwidth, imgheight = im.size
    for i in range(0,imgheight,height):
        for j in range(0,imgwidth,width):
            box = (j, i, j+width, i+height)
            a = im.crop(box)
            a.save(path + "crack_" + str(i) + "_" + str(j)+".jpg")


path = "E:/PyCharm Community Edition 2021.3.1/probility/Crack-Detection/sample_dataset/"
input = "E:/PyCharm Community Edition 2021.3.1/probility/crack detection/Picture2.jpg"

cr = crop(path,input,100,100)