import io
from .node import Node


class Beam:
    Id: int
    I: Node
    J: Node

    def __init__(self, Id: int, i: Node, j: Node):
        self.Id = int(Id)
        self.I = i
        self.J = j

    def write(self, file: io.TextIOWrapper):
        file.write(f"{self.Id} {self.I.Id} {self.J.Id};\n")

    def __str__(self) -> str:
        return f"{self.Id}:{self.I.Id} {self.J.Id}"
