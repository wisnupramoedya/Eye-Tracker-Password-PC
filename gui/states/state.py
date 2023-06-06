from typing import List
from gui.data.Icons import MaterialIcon

class Coordinate:
    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f'x: {self.x}; y: {self.y}'

class Password:
    icon: MaterialIcon
    coordinate: Coordinate

    def __init__(self, icon: MaterialIcon, coordinate: Coordinate) -> None:
        self.icon = icon
        self.coordinate = coordinate

class State:
    set_sequence_coor: Coordinate
    set_sequence_index: int

    password_sequences: List[Password] = list()