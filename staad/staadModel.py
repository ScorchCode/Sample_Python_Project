from datetime import datetime
from staad.elements import Node, Beam
from staad.sections import RectangleSection


class StaadModel:
    Nodes: list[Node] = []
    Beams: list[Beam] = []
    RectangleSections: list[RectangleSection] = []

    def PrintModel(self):
        file = open("PileGroup.std", "w")
        file.write("STAAD SPACE\n")
        file.write("START JOB INFORMATION\n")
        file.write(f"ENGINEER DATE {datetime.today().strftime('%d-%b-%y')}\n")
        file.write("END JOB INFORMATION\n")
        file.write("INPUT WIDTH 79\n")
        file.write("UNIT METER MTON\n")

        # Code to print Joint coordinates
        file.write("JOINT COORDINATES\n")

        for node in self.Nodes:
            node.write(file)

        # Code to print Beams
        file.write("MEMBER INCIDENCES\n")
        for beam in self.Beams:
            beam.write(file)

        # Code to print material properties
        file.write("DEFINE MATERIAL START\n")
        file.write("ISOTROPIC CONCRETE\n")
        file.write("E  200000\n")
        file.write("POISON  0.2\n")
        file.write("DENSITY  2.5\n")
        file.write("ALPHA  1e-05\n")
        file.write("DAMP  0.05\n")
        file.write("END DEFINE MATERIAL\n")
        file.write("CONSTANTS \n")
        file.write("MATERIAL CONCRETE ALL\n")

        # Code to print member properties
        file.write("MEMBER PROPERTY INDIAN\n")
        for section in self.RectangleSections:
            section.write(file)

        file.write("PERFORM ANALYSIS\n")
        file.write("FINISH\n")

        file.close
