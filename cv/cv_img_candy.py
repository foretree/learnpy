# coding:utf8

import cv2

if __name__ == '__main__':
    img = cv2.imread('test.jpg')
    cv2.imshow('candy', cv2.Canny(img, 50, 100))
    cv2.waitKey(0)
    cv2.destroyAllWindows()
