import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import QGroupBox, QLabel, QSizePolicy
from PyQt6.QtGui import QCursor, QPixmap
from gui.states.state import Password, Coordinate

class PasswordWidget(QGroupBox):
    name_label: QLabel
    coor_label: QLabel
    delete_label: QLabel

    def __init__(self, password: Password, *args, **kwargs) -> None:
        super(PasswordWidget, self).__init__(*args, **kwargs)
        self.setSizePolicy(
            QSizePolicy.Policy.Preferred,
            QSizePolicy.Policy.Fixed)
        self.setMinimumSize(711, 160)
        self.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.setAutoFillBackground(False)
        self.setStyleSheet("background: #2F2F3B;")
        self.setPasswordName(password.icon.icon_name)
        self.setPasswordCoor(password.coordinate)
        self.setPasswordDelete()
    
    def setPasswordName(self, text):
        label: QLabel = QLabel(self)
        label.setGeometry(10, 51, 481, 41)
        label.setStyleSheet("font-weight: 600; font-size: 32px; line-height: 140%; text-align: center; letter-spacing: 0.01em; color: #F88160;")
        label.setText(text)
        label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)

        self.name_label = label

    def setPasswordCoor(self, coordinate: Coordinate):
        label: QLabel = QLabel(self)
        label.setGeometry(10, 90, 491, 41)
        label.setText(coordinate.__str__())
        label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)

        self.coor_label = label

    def setPasswordDelete(self):
        label: QLabel = QLabel(self)
        label.setGeometry(630, 40, 61, 71)
        label.setCursor(QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        file = 'gui\\assets\\images\\ic-trash.png'
        label.setPixmap(QPixmap(file))
        # label.setText("Halo")
        label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.delete_label = label
