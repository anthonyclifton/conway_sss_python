class Grid(object):
    def __init__(self):
        self.cells = set()

    def birth_cell(self, coordinates):
        self.cells.add(coordinates)

    def birth_cells(self, cells):
        for cell in cells:
            self.birth_cell(cell)

    def kill_cell(self, coordinates):
        self.cells.remove(coordinates)

    def get_cells(self):
        return self.cells
