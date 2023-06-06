from pathlib import Path

from PyQt6 import QtGui
from PyQt6.QtCore import QEvent, QObject, Qt, QSize
from PyQt6.QtWidgets import QWidget, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea, QGridLayout, QLayoutItem
from PyQt6.uic import loadUi

import qtawesome
from gui.data.ScreenConst import ScreenConst
from gui.window import Window
from settings import Settings
from gui.data.Icons import MaterialIcon, material_icon_codes
from typing import List

from gui.states.state import Coordinate, State, Password

class SetSequenceScreen(QMainWindow):
    # Path for UI and index setting
    FILE_PATH: Path = Settings.ASSETS / "SetSequence.ui"
    controller_widget: Window

    scrollArea: QScrollArea
    gridLayout: QGridLayout

    icons: List[MaterialIcon]

    def __init__(self, controller_widget: Window):
        super(SetSequenceScreen, self).__init__()
        self.controller_widget = controller_widget
        loadUi(self.FILE_PATH, self)
        self.createPopupBox()
        self.createClickable()
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

    def setIcon(self, index: int):
        state = self.controller_widget.state

        for x in range(4):
            for y in range(4):
                grid_item: QLayoutItem = self.gridLayout.itemAtPosition(x, y)
                label: QLabel = grid_item.widget()
                label.clear()

        if index != -1:
            grid_item: QLayoutItem = self.gridLayout.itemAtPosition(state.set_sequence_coor.x, state.set_sequence_coor.y)
            label: QLabel = grid_item.widget()

            label.setPixmap(qtawesome.icon(state.password_sequences[state.set_sequence_index].icon.icon_code).pixmap(QSize(100, 100)))
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)


    def setLabelMouseEvent(self, x: int, y: int):
        state: State = self.controller_widget.state
        state.set_sequence_coor = Coordinate(x, y)
        self.scrollArea.setVisible(True)

    def setPopupLabelMouseEvent(self, icon: MaterialIcon):
        state: State = self.controller_widget.state
        if state.set_sequence_index == -1:
            state.password_sequences.append(Password(icon, state.set_sequence_coor))
        else:
            password = state.password_sequences[state.set_sequence_index]
            password.icon = icon
            password.coordinate = state.set_sequence_coor
        
        self.scrollArea.setVisible(False)

        
        from gui.screens.configure_screens.configuration_screen import ConfigurationScreen
        configuration_screen: ConfigurationScreen = self.controller_widget.widget(ScreenConst.CONFIGURATION_SCREEN)
        configuration_screen.getBlueprint()
        self.controller_widget.setCurrentIndex(ScreenConst.CONFIGURATION_SCREEN)

    def createClickable(self):
        for x in range(4):
            for y in range(4):
                grid_item: QLayoutItem = self.gridLayout.itemAtPosition(x, y)
                label: QLabel = grid_item.widget()

                label.setCursor(QtGui.QCursor(Qt.CursorShape.PointingHandCursor))
                label.mouseReleaseEvent = lambda event, x = x, y = y: self.setLabelMouseEvent(x, y)

    def createPopupBox(self):
        self.icons = material_icon_codes.copy()
        self.scrollArea = QScrollArea(self)
        self.scrollWidget = QWidget()
        self.scrollVBox = QVBoxLayout()

        for icon in self.icons:
            widget = QWidget()
            boxLayout = QHBoxLayout()
            
            iconLabel = QLabel()
            iconLabel.setPixmap(qtawesome.icon(icon.icon_code).pixmap(QSize(60, 60)))
            iconLabel.setStyleSheet('color: #2F2F3B')

            nameLabel = QLabel(icon.icon_name)
            nameLabel.setStyleSheet('color: #2F2F3B; font-size: 30px')

            boxLayout.addStretch()
            boxLayout.addWidget(iconLabel)
            boxLayout.addWidget(nameLabel)
            boxLayout.addStretch()
            widget.setLayout(boxLayout)
            widget.setCursor(QtGui.QCursor(Qt.CursorShape.PointingHandCursor))
            widget.mouseReleaseEvent = lambda event, icon = MaterialIcon(icon.icon_name, icon.icon_code): self.setPopupLabelMouseEvent(icon)

            self.scrollVBox.addWidget(widget)
        
        self.scrollWidget.setLayout(self.scrollVBox)

        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.scrollWidget)
        self.scrollArea.raise_()
        self.scrollArea.setStyleSheet('background: #FFFFFF;')
        self.scrollArea.setGeometry(304, 231, 671, 465)
        self.scrollArea.setVisible(False)
        
    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.key() == Qt.Key.Key_Space:
            pass