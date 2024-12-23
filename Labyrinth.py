from dataclasses import dataclass

@dataclass
class Cell:
    x: int
    y: int
    type: str  # '.', '#', 'F', 'D', 'S'