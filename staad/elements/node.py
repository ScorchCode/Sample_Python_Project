import io


class Node:
    Id: int
    X: float
    Y: float
    Z: float

    def __init__(self, Id: int, x: float, y: float, z: float):
        self.Id = int(Id)
        self.X = float(x)
        self.Y = float(y)
        self.Z = float(z)

    def write(self, file: io.TextIOWrapper):
        file.write(f"{self.Id},{self.X:0.4f},{self.Y:0.4f},{self.Z:0.4f};\n")

    def __str__(self) -> str:
        return f"{self.Id}:{self.X},{self.Y},{self.Z}"
