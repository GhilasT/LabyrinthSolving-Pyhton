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
        
    # Permet de trouver les cellules de départ et de Sortie    
    def _find_position(self, char: str) -> Cell:
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == char:
                    return Cell(x, y, char)
        return None
