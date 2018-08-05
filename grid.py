class Grid(object):
    def __init__(self):
        self.cells = []

    def birth_cell(self, coordinates):
        self.cells.append(coordinates)
