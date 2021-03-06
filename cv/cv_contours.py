# coding:utf8

import cv2
import numpy as np

if __name__ == '__main__':
    img = cv2.pyrDown(cv2.imread('test.jpg', cv2.IMREAD_UNCHANGED))
    ret, thresh = cv2.threshold(cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY),
                                127, 255, cv2.THRESH_BINARY)
    image, contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        # opencv 4.2.0不能用了
        print(cv2.boundingRect(c))
        # x,y,w,h = cv2.boundingRect(c)
    #     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #
    #     rect = cv2.minAreaRect(c)
    #     box = np.int0(cv2.boxPoints(rect))
    #     cv2.drawContours(img, [box], 0, (0,0,255), 3)
    #     (x,y),radius = cv2.minEnclosingCircle(c)
    #     center = (int(x), int(y))
    #     radius = int(radius)
    #
    #     cv2.circle(img, center, radius, (255, 0, 0), 2)
    #
    # cv2.drawContours(img, contours, -1, (255, 0, 0), 1)
    # cv2.imshow('contours', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
