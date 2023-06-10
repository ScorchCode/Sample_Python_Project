import io
from elements.beam import Beam


class RectangleSection:
    Width: float
    Depth: float
    Beams: list[Beam] = []

    def __init__(self, width: float, depth: float):
        self.Width = width
        self.Depth = depth

    def write(self, file: io.TextIOWrapper):
        file.write(f"{self.Beams[0].Id} To {self.Beams[-1].Id} -\n")
        file.write(f"PRIS YD {self.Depth:0.4f} ZD {self.Width:0.4f}\n")

    def __str__(self) -> str:
        return f"Width:{self.Width:0.4f} | Depth:{self.Depth:0.4f}"
