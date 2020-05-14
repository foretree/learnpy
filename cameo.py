# coding:utf8

import cv2
import cv.filters as filters
from cv.utils import detectDrawRectangle
from cv.cv_hog import detect_person
from cv.camera_managers import CaptureManager, WindowManager


class Cameo(object):

    def __init__(self):
        self._windowManager = WindowManager('Cameo', self.onKeypress)
        self._captureManager = CaptureManager(cv2.VideoCapture(0), self._windowManager, True)

        self._curveFilter = filters.EmbossedFilter()

    def run(self):
        self._windowManager.createWindow()

        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            frame = self._captureManager.frame

            # filter
            # filters.strokeEdges(frame, frame)
            # self._curveFilter.apply(frame, frame)

            # face detect
            frame = detectDrawRectangle(frame)

            # object detect
            # frame = detect_person(frame)

            self._windowManager.show(frame)
            self._captureManager.exitFrame()
            self._windowManager.processEvents()

    def onKeypress(self, keycode):

        if keycode == 32:  # space
            self._captureManager.writeImage('screenshot.png')
        elif keycode == 9:  # tab
            if self._captureManager.isWritingVideo:
                self._captureManager.stopWritingVideo()
            else:
                self._captureManager.startWritingVideo('screencast.avi')
        elif keycode == 27:  # escape
            self._windowManager.destroyWindow()


if __name__ == '__main__':
    Cameo().run()
