from pathlib import Path

from PyQt6 import QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow
from PyQt6.uic import loadUi

from gui.data.ScreenConst import ScreenConst
from gui.window import Window
from settings import Settings


class SuccessScreen(QMainWindow):
    # Path for UI and index setting
    FILE_PATH: Path = Settings.ASSETS / "Response.ui"
    controller_widget: Window

    def __init__(self, controller_widget: Window):
        super(SuccessScreen, self).__init__()
        self.controller_widget = controller_widget
        loadUi(self.FILE_PATH, self)
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.key() == Qt.Key.Key_Space:
            self.controller_widget.setCurrentIndex(ScreenConst.CALIBRATION_SCREEN)
