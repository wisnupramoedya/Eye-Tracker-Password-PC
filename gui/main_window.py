from typing import List

from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QWidget

from capturers import Capture
from frame_sources import FrameSource
from gui.screens.calibration_screen import CalibrationScreen
from gui.data.ScreenConst import ScreenConst
from gui.screens.password_screen import PasswordScreen
from gui.screens.success_screen import SuccessScreen
from gui.window import Window
from settings import settings


class MainWindow(Window):
    screens: List[QWidget]
    capture: Capture

    timer: QTimer = None

    def __init__(self, capture: Capture, video_source: FrameSource = None):
        super(MainWindow, self).__init__(capture, video_source)
        self.capture = capture
        self.video_source = video_source
        self.set_screens()
        self.start()

    def set_screens(self):
        self.addWidget(CalibrationScreen(controller_widget=self))
        self.addWidget(PasswordScreen(controller_widget=self))
        self.addWidget(SuccessScreen(controller_widget=self))
        self.setCurrentIndex(ScreenConst.CALIBRATION_SCREEN)

    def start(self):
        self.video_source.start()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(settings.REFRESH_PERIOD)

    def stop(self):
        self.timer.stop()
        self.video_source.stop()

    def update_frame(self):
        frame = self.video_source.next_frame()
        face, l_eye, r_eye = self.capture.process(frame, 50, 50)

