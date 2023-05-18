from elements import Node


class StaadModel:

    Nodes: list[Node] = []

    def printmodel(self):
        file = open("PileGroup.std", "w")
        file.write("STAAD SPACdE\n")

        # Code to print Joint coordinates
        file.write("JOINT COORDINATES\n")

        # for node in self.Nodes:
        #     node.write(file)

        file.write("FINISH\n")

        file.close()
