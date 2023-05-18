from staad import StaadModel
from staad import Node


model = StaadModel()

n1 = Node(1, 0, 0, 0)
n2 = Node(1, 10, 0, 0)
model.Nodes.append(n1)
model.Nodes.append(n2)

# b = Beam(1, n1, n2)
model.printmodel()
