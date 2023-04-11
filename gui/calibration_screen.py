from pathlib import Path
from typing import List

from PyQt6 import QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QFrame, QStackedWidget, QMainWindow
from PyQt6.uic import loadUi

from capturers import Capture
from frame_sources import FrameSource
from gui.data.ScreenConst import ScreenConst
from settings import Settings


class CalibrationScreen(QMainWindow):
    # Path for UI and index setting
    FILE_PATH: Path = Settings.ASSETS / "Calibration.ui"
    controller_widget: QStackedWidget

    # Labelling the frame in grid layout for calibration (it will be dynamically detected)
    gl_11: QLabel
    gl_15: QLabel
    gl_51: QLabel
    gl_55: QLabel

    # Listing for widget variable that requires to be located
    widget_show_lists: List[QFrame]
    widget_index: int = 0

    def __init__(self, capture: Capture, controller_widget: QStackedWidget, video_source: FrameSource = None):
        super(CalibrationScreen, self).__init__()
        self.controller_widget = controller_widget
        loadUi(self.FILE_PATH, self)
        self.set_widget_list()
        self.set_color_widget()
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

    def set_widget_list(self):
        self.widget_show_lists = [
            self.gl_11,
            self.gl_15,
            self.gl_55,
            self.gl_51
        ]

    def set_color_widget(self):
        for i in range(4):
            if i == self.widget_index:
                self.widget_show_lists[i].setStyleSheet('background-color: rgb(217, 217, 217);')
            else:
                self.widget_show_lists[i].setStyleSheet('background-color: rgb(28, 28, 37);')

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.key() == Qt.Key.Key_Space:
            self.widget_index += 1
            if self.widget_index == 4:
                self.widget_index = 0

            self.set_color_widget()

            if self.widget_index == 0:
                self.controller_widget.setCurrentIndex(ScreenConst.PASSWORD_SCREEN)
