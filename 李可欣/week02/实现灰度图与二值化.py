import cv2#opencv读取的格式是BGR
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread('lenna.png')

cv2.imshow('Gray image',img) #显示灰度图像
cv2.imshow('binary image',binaryImg) #显示二值化图像
