from typing import Tuple
import math

def counter_mid_point(
        left_pupil: Tuple[int, int] | None,
        right_pupil: Tuple[int, int] | None
        ) -> Tuple[int, int] | None:
    if left_pupil is not None and right_pupil is not None:
        x_mid = round((left_pupil[0] + right_pupil[0]) / 2)
        y_mid = round((left_pupil[1] + right_pupil[1]) / 2)
        return (x_mid, y_mid)