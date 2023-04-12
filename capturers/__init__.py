from typing import Protocol, Optional

import numpy


class Capture(Protocol):
    def detect_eyes(
            self, face_img: numpy.ndarray, cut_brows=True
    ) -> (Optional[numpy.ndarray], Optional[numpy.ndarray]):
        ...

    def detect_face(self, img: numpy.ndarray) -> Optional[numpy.ndarray]:
        ...

    def process(self, frame: numpy.ndarray, l_threshold, r_threshold):
        ...
