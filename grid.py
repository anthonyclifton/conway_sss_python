class Generation():
    def __init__(self, live_cells={}, dead_cells={}):
        self.live_cells = set(live_cells)
        self.dead_cells = set(dead_cells)

    def __eq__(self, other):
        return self.live_cells == other.live_cells and \
               self.dead_cells == other.dead_cells

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return "Live Cells: " + str(self.live_cells) + "\nDead Cells: " + str(self.dead_cells)

    def __repr__(self):
        return "Live Cells: " + str(self.live_cells) + "\nDead Cells: " + str(self.dead_cells)

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

    def generate_next_generation(self):
        generation = Generation()
        for cell in self.cells:
            count = 0
            y, x = cell
            if (y-1, x) in self.cells:
                count += 1
            if (y+1, x) in self.cells:
                count += 1
            if (y, x-1) in self.cells:
                count += 1
            if (y, x+1) in self.cells:
                count += 1
            if (y-1, x-1) in self.cells:
                count += 1
            if (y+1, x+1) in self.cells:
                count += 1
            if (y-1, x+1) in self.cells:
                count += 1
            if (y+1, x-1) in self.cells:
                count += 1

            if count == 2 or count == 3:
                generation.live_cells.add(cell)
            else:
                generation.dead_cells.add(cell)

        return generation
        #if len(self.cells) == 3:
        #    return Generation({(1, 1)}, {(0, 0), (2, 2)})
        #elif len(self.cells) == 4:

        #return Generation()
