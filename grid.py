class Grid(object):
    def __init__(self):
        self.cells = set()

    def birth_cell(self, coordinates):
        self.cells.add(coordinates)

    def kill_cell(self, coordinates):
        self.cells.remove(coordinates)

    def count_neighbors(self, coordinates):
        return len([cell for cell in self.cells if self._are_neighbors(coordinates, cell)])

    def get_adjacent_empty_cells(self, coordinates):
        cell_y, cell_x = coordinates
        possible_cells = [(y, x)
                          for x in range(cell_x - 1, cell_x + 2, 1)
                          for y in range(cell_y - 1, cell_y + 2, 1)]
        return [cell for cell in possible_cells
                if cell != coordinates
                and not self._is_alive(cell)]

    @staticmethod
    def _are_neighbors(cell_to_check, possible_neighbor):
        x_distance = abs(cell_to_check[1] - possible_neighbor[1])
        y_distance = abs(cell_to_check[0] - possible_neighbor[0])
        return x_distance == 1 or y_distance == 1

    def _is_alive(self, coordinates):
        return coordinates in self.cells
