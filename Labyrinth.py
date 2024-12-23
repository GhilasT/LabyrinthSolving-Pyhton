from dataclasses import dataclass

@dataclass
class Cell:
    x: int
    y: int
    type: str  # '.', '#', 'F', 'D', 'S'
    
    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        if not isinstance(other, Cell):
            return False
        return self.x == other.x and self.y == other.y


class Labyrinth:
    def __init__(self, grid: List[List[str]]):
        self.height = len(grid)
        self.width = len(grid[0])
        self.grid = [row[:] for row in grid]  # Deep copy of the grid