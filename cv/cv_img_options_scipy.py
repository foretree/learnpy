# coding:utf8

import cv2
import numpy as np
from scipy import ndimage

if __name__ == '__main__':
    kernel_3x3 = np.array([
        [-1, -1, -1],
        [-1, 8, -1],
        [-1, -1, -1],
    ])
    kernel_5x5 = np.array([
        [-1, -1, -1, -1, -1],
        [-1, 1, 2, 1, -1],
        [-1, 2, 4, 2, -1],
        [-1, 1, 2, 1, -1],
        [-1, -1, -1, -1, -1],
    ])

    img = cv2.imread('test.jpg', 0)

    k3 = ndimage.convolve(img, kernel_3x3)
    k5 = ndimage.convolve(img, kernel_5x5)

    blur = cv2.GaussianBlur(img, (11, 11), 0)
    g_guess = img - blur

    cv2.imshow('1', k3)
    cv2.imshow('2', k5)
    cv2.imshow('3', g_guess)
    cv2.imshow('blur', blur)

    cv2.waitKey()
    cv2.destroyAllWindows()
