class Grid(object):
    def __init__(self):
        self.cells = set()

    def birth_cell(self, coordinates):
        self.cells.add(coordinates)

    def kill_cell(self, coordinates):
        self.cells.remove(coordinates)
