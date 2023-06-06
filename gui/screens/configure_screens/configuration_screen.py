from pathlib import Path

from PyQt6 import QtGui
from PyQt6.QtCore import QEvent, QObject, Qt
from PyQt6.QtWidgets import QWidget, QMainWindow, QVBoxLayout, QLabel
from PyQt6.uic import loadUi

from gui.data.ScreenConst import ScreenConst
from gui.window import Window
from settings import Settings

from gui.components.configuration.password_widget import PasswordWidget


class ConfigurationScreen(QMainWindow):
    # Path for UI and index setting
    FILE_PATH: Path = Settings.ASSETS / "Configuration.ui"
    controller_widget: Window

    verticalLayout: QVBoxLayout

    def __init__(self, controller_widget: Window):
        super(ConfigurationScreen, self).__init__()
        self.controller_widget = controller_widget
        loadUi(self.FILE_PATH, self)
        self.addRoute()
        self.getBlueprint()
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
    
    def setButtonEvent(self, event, index):
        state = self.controller_widget.state
        state.set_sequence_index = index

        if index != -1:
            state.set_sequence_coor = state.password_sequences[state.set_sequence_index].coordinate
            
        from gui.screens.configure_screens.set_sequence_screen import SetSequenceScreen
        set_sequence_screen: SetSequenceScreen = self.controller_widget.widget(ScreenConst.SET_SEQUENCE_SCREEN)
        set_sequence_screen.setIcon(index)

        self.controller_widget.setCurrentIndex(ScreenConst.SET_SEQUENCE_SCREEN)

    def addRoute(self):
        self.add_btn.mouseReleaseEvent = lambda event: self.setButtonEvent(event, -1)

    def setRoute(self, index: int):
        self.controller_widget.setCurrentIndex(index)

    def deleteButtonEvent(self, event, index):
        state = self.controller_widget.state
        state.password_sequences.pop(index)

        self.getBlueprint()

    def getBlueprint(self):
        # for i in reversed(range(self.verticalLayout.count())):
        #     widgetToRemove = self.verticalLayout.itemAt(i).widget()
        #     self.verticalLayout.removeWidget(widgetToRemove)
        #     widgetToRemove.setParent(None)

        while self.verticalLayout.count():
            child = self.verticalLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        self.verticalLayout.addStretch()
        state = self.controller_widget.state

        for index, password in enumerate(state.password_sequences):
            widget_item: PasswordWidget = PasswordWidget(password=password)
            widget_item.mouseReleaseEvent = lambda event, index = index: self.setButtonEvent(event, index)
            widget_item.delete_label.mouseReleaseEvent = lambda event, index = index: self.deleteButtonEvent(event, index)
            self.verticalLayout.insertWidget(self.verticalLayout.count() - 1, widget_item)

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.key() == Qt.Key.Key_Space:
            pass