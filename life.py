from collections import defaultdict
from ast import literal_eval

class Life():
    def __init__(self, starting_cells=None):
        if starting_cells is not None:
            self.cells = starting_cells
        else:
            filename = "gosper_gun.txt"
            starting_cells = []
            with open(filename, 'r') as in_file:
                for line in in_file.readlines():
                    if line[0] == '(':
                        starting_cells.append(literal_eval(line))
            self.cells = starting_cells

    def next(self):
        cell_neighbors = defaultdict(int)
        for cell in self.cells:
            self._mark_neighbors(cell, cell_neighbors)

        next_cells = []
        for cell, neighbor_count in cell_neighbors.items():
            if self._is_alive(cell) and neighbor_count in (2, 3):
                next_cells.append(cell)
            if not self._is_alive(cell) and neighbor_count == 3:
                next_cells.append(cell)

        self.cells = next_cells
        return self.cells

    def _mark_neighbors(self, cell, cell_neighbors):
        row, col = cell
        cell_neighbors[(row-1, col-1)]+=1
        cell_neighbors[(row-1, col)]+=1
        cell_neighbors[(row-1, col+1)]+=1
        cell_neighbors[(row, col+1)]+=1
        cell_neighbors[(row, col-1)]+=1
        cell_neighbors[(row+1, col-1)]+=1
        cell_neighbors[(row+1, col)]+=1
        cell_neighbors[(row+1, col+1)]+=1

    def _is_alive(self, cell):
        return cell in self.cells

