from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import QStackedWidget

from capturers import Capture
from frame_sources import FrameSource


class Window(QStackedWidget):
    timer: QTimer

    def __init__(self, capture: Capture, video_source: FrameSource = None):
        super(Window, self).__init__()
        ...

    def set_screens(self):
        ...

    def start(self):
        ...

    def stop(self):
        ...

    def update_frame(self):
        ...