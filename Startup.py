from staad import StaadModel
from staad.elements import Node, Beam
model = StaadModel()

n1 = Node(1, 10, 0, 0)
n2 = Node(2, 20, 0, 0)
n3 = Node(3, 30, 0, 0)

model.Nodes.append(n1)
model.Nodes.append(n2)
model.Nodes.append(n3)

b1 = Beam(1, n1, n2)
b2 = Beam(2, n2, n3)
model.Beams.append(b1)
model.Beams.append(b2)

model.PrintModel()
