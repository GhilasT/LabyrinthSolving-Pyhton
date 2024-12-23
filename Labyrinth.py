from dataclasses import dataclass

@dataclass
class Cell:
    x: int
    y: int
    type: str  # '.', '#', 'F', 'D', 'S'
    
    def __hash__(self):
        return hash((self.x, self.y))