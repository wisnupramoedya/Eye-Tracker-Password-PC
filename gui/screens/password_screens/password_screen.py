from pathlib import Path
from typing import List

import qtawesome
from PyQt6 import QtGui
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QMainWindow, QLabel, QGridLayout, QLayoutItem
from PyQt6.uic import loadUi

from gui.data.Icons import MaterialIcon, Icons
from gui.data.ScreenConst import ScreenConst
from gui.window import Window
from settings import Settings


class PasswordEvent:
    def __init__(self, title: str, instruction: str):
        self.title = title
        self.instruction = instruction


class PasswordScreen(QMainWindow):
    # Path for UI and index setting
    FILE_PATH: Path = Settings.ASSETS / "Password.ui"
    controller_widget: Window

    title: QLabel
    instruction: QLabel
    gridLayout: QGridLayout

    icons: List[MaterialIcon]

    password_event: List[PasswordEvent] = [
        PasswordEvent("Check Password 1 - Icon Location", "Press “space” when your eyes look at the correct icon"),
        PasswordEvent("Check Password 2 - Real Location", "Press “space” when your eyes look at the correct position")
    ]
    event_index: int = 0

    def __init__(self, controller_widget: Window):
        super(PasswordScreen, self).__init__()
        self.controller_widget = controller_widget
        loadUi(self.FILE_PATH, self)
        self.icons = Icons.generate_random_icon()
        self.set_password_event()
        self.set_grid_layout_images()
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.key() == Qt.Key.Key_Space:
            self.event_index += 1
            if self.event_index == len(self.password_event):
                self.event_index = 0

            self.set_password_event()

            if self.event_index == 0:
                self.icons = Icons.generate_random_icon()
                self.controller_widget.setCurrentIndex(ScreenConst.SUCCESS_SCREEN)

    def set_password_event(self):
        self.title.setText(self.password_event[self.event_index].title)
        self.instruction.setText(self.password_event[self.event_index].instruction)
        

    def set_grid_layout_images(self):
        for x in range(4):
            for y in range(4):
                grid_item: QLayoutItem = self.gridLayout.itemAtPosition(x, y)
                label: QLabel = grid_item.widget()

                position = x * 4 + y
                label.setPixmap(qtawesome.icon(self.icons[position].icon_code).pixmap(QSize(100, 100)))
                label.setAlignment(Qt.AlignmentFlag.AlignCenter)
