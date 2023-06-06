from typing import List

from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QWidget

from capturers import Capture
from frame_sources import FrameSource
from gui.data.ScreenConst import ScreenConst
from gui.screens.password_screens.calibration_screen import CalibrationScreen
from gui.screens.password_screens.password_screen import PasswordScreen
from gui.screens.password_screens.success_screen import SuccessScreen
from gui.screens.landing_screen import LandingScreen
from gui.screens.configure_screens.configuration_screen import ConfigurationScreen
from gui.screens.configure_screens.set_sequence_screen import SetSequenceScreen
from gui.window import Window
from settings import settings
from gui.pupil_check import PupilWindow
from gui.states.state import State


class MainWindow(Window):
    screens: List[QWidget]
    capture: Capture
    pupil_window: PupilWindow

    def __init__(self, capture: Capture, video_source: FrameSource = None):
        super(MainWindow, self).__init__(capture, video_source)
        self.capture = capture
        self.video_source = video_source
        self.pupil_window = PupilWindow()
        self.state = State()
        self.set_screens()
        self.start()

    def set_screens(self):
        self.addWidget(LandingScreen(controller_widget=self))
        self.addWidget(CalibrationScreen(controller_widget=self))
        self.addWidget(PasswordScreen(controller_widget=self))
        self.addWidget(SuccessScreen(controller_widget=self))
        self.addWidget(ConfigurationScreen(controller_widget=self))
        self.addWidget(SetSequenceScreen(controller_widget=self))
        self.setCurrentIndex(ScreenConst.LANDING_SCREEN)

    def start(self):
        self.video_source.start()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(10)

    def stop(self):
        self.timer.stop()
        self.video_source.stop()

    def update_frame(self):
        frame = self.video_source.next_frame()
        self.pupil_window.process(frame)
        # face, l_eye, r_eye = self.capture.process(frame, 50, 50)

