import argparse
import logging
import sys

from PyQt6.QtWidgets import QApplication

from capturers.haar_blob import HaarCascadeBlobCapture
from frame_sources import (CameraFrameSource, FileFrameSource,
                           FolderFrameSource, VideoFrameSource)
from gui.camera_window import CameraWindow
from gui.main_window import MainWindow

FRAME_SOURCES = {
    "camera": CameraFrameSource,
    "folder": FolderFrameSource,
    "file": FileFrameSource,
    "video": VideoFrameSource,
}


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-fs",
        "--frame-source",
        action="store",
        dest="frame_source",
        choices=FRAME_SOURCES.keys(),
        default="camera",
        help="What should be the frames source. A video/file, a folder with frames or a camera",
    )
    parser.add_argument(
        "-cam-id",
        "--camera-id",
        action="store",
        dest="camera_id",
        # choices=FRAME_SOURCES.keys(),
        help="If your camera has an unusual ID in the system, pass it in this argument. Use only if your frame-source "
             "is camera(default)",
    )

    args = parser.parse_args()

    return args


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, filename="logfile", filemode="a+",
                        format="%(asctime)-15s %(levelname)-8s %(message)s")
    args = get_args()
    frame_source = FRAME_SOURCES[args.frame_source]

    frames_source_init_kwargs = {}
    if args.camera_id and args.frame_source == "camera":
        frames_source_init_kwargs["cam_id"] = args.camera_id

    capture = HaarCascadeBlobCapture()

    app = QApplication(sys.argv)

    window = MainWindow(capture, frame_source(**frames_source_init_kwargs))
    window.setWindowTitle("Eye Tracking Password")
    window.setFixedWidth(1280)
    window.setFixedHeight(832)
    window.show()

    # window = CameraWindow(capture, frame_source(**frames_source_init_kwargs))
    # window.setWindowTitle("Eye Tracking Password - Camera")
    # window.show()

    sys.exit(app.exec())
