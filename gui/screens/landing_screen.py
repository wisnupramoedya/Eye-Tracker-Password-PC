from pathlib import Path
from typing import List

from PyQt6 import QtGui
from PyQt6.QtCore import QEvent, QObject, Qt
from PyQt6.QtWidgets import QWidget, QMainWindow
from PyQt6.uic import loadUi

from gui.data.ScreenConst import ScreenConst
from gui.window import Window
from settings import Settings


class LandingScreen(QMainWindow):
    # Path for UI and index setting
    FILE_PATH: Path = Settings.ASSETS / "Landing.ui"
    controller_widget: Window

    configure_btn: QWidget
    password_btn: QWidget

    def __init__(self, controller_widget: Window):
        super(LandingScreen, self).__init__()
        self.controller_widget = controller_widget
        loadUi(self.FILE_PATH, self)
        self.addRoute()
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

    def addRoute(self):
        self.configure_btn.mouseReleaseEvent = lambda event: self.controller_widget.setCurrentIndex(ScreenConst.CONFIGURATION_SCREEN)
        self.password_btn.mouseReleaseEvent = lambda event: self.controller_widget.setCurrentIndex(ScreenConst.CALIBRATION_SCREEN)

    def setRoute(self, index: int):
        self.controller_widget.setCurrentIndex(index)

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.key() == Qt.Key.Key_Space:
            pass