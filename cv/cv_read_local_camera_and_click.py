# coding:utf8

import cv2


class LocalCamera:
    def __init__(self):
        self.clicked = False

    def onClick(self, event, x, y, flags, params):
        if event == cv2.EVENT_LBUTTONUP:
            self.clicked = True

    def start(self):
        capture = cv2.VideoCapture(0)
        cv2.namedWindow('window')
        cv2.setMouseCallback('window', self.onClick)
        print('showing camera feed, click window or press any key to stop')
        success, frame = capture.read()
        while success and cv2.waitKey(1) == -1 and not self.clicked:
            cv2.imshow('window',frame)
            success, frame = capture.read()
        print('close window and release capture')
        cv2.destroyWindow('window')
        capture.release()


if __name__ == '__main__':
    c = LocalCamera()
    c.start()
