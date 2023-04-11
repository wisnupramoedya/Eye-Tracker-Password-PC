from typing import List

from PyQt6 import QtGui, QtCore
from PyQt6.QtWidgets import QStackedWidget, QWidget

from capturers import Capture
from frame_sources import FrameSource
from gui.calibration_screen import CalibrationScreen
from gui.data.ScreenConst import ScreenConst
from gui.password_screen import PasswordScreen


class MainWindow(QStackedWidget):
    screens: List[QWidget]
    capture: Capture

    def __init__(self, capture: Capture, video_source: FrameSource = None):
        super(MainWindow, self).__init__()
        self.capture = capture
        self.set_screens()

    def set_screens(self):
        self.addWidget(CalibrationScreen(capture=self.capture, controller_widget=self))
        self.addWidget(PasswordScreen(capture=self.capture, controller_widget=self))
        self.setCurrentIndex(ScreenConst.PASSWORD_SCREEN)

