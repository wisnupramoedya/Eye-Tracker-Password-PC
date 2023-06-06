"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import cv2
from gaze_tracking.gaze_tracking import GazeTracking
import numpy
from typing import Tuple

class PupilWindow():
    gaze: GazeTracking
    left_pupil: Tuple[int, int]
    right_pupil: Tuple[int, int]
    
    def __init__(self) -> None:
        self.gaze = GazeTracking()
        self.left_pupil = (0, 0)
        self.right_pupil = (0, 0)
        
    def process(self, frame: numpy.ndarray):
        # We send this frame to GazeTracking to analyze it
        self.gaze.refresh(frame)

        frame = self.gaze.annotated_frame()
        text = ""

        if self.gaze.is_blinking():
            text = "Blinking"
        elif self.gaze.is_right():
            text = "Looking right"
        elif self.gaze.is_left():
            text = "Looking left"
        elif self.gaze.is_center():
            text = "Looking center"

        cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)
        
        temp_left_pupil = self.gaze.pupil_left_coords()
        if temp_left_pupil is not None:
            self.left_pupil = temp_left_pupil
        
        temp_right_pupil = self.gaze.pupil_right_coords()
        if temp_right_pupil is not None:
            self.right_pupil = temp_right_pupil
            
        cv2.putText(frame, "Left pupil:  " + str(self.left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
        cv2.putText(frame, "Right pupil: " + str(self.right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

        cv2.imshow("Demo", frame)
   

