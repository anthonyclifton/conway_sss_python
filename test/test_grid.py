import unittest
from grid import Grid


class TestGrid(unittest.TestCase):
    def setUp(self):
        self.grid = Grid()

    def test__grid__should_birth_cell(self):
        expected_cell = (0, 0)
        self.grid.birth_cell(expected_cell)
        assert expected_cell in self.grid.cells

    def test__grid__should_not_allow_duplicate_cells(self):
        cell_to_birth = (0, 0)
        self.grid.birth_cell(cell_to_birth)
        self.grid.birth_cell(cell_to_birth)
        self.assertEquals(len(self.grid.cells), 1)

    def test__grid__should_kill_cell(self):
        cell_to_kill = (0, 0)
        self.grid.birth_cell(cell_to_kill)
        assert cell_to_kill in self.grid.cells

        self.grid.kill_cell(cell_to_kill)
        assert cell_to_kill not in self.grid.cells

    def test__grid__should_set_cells(self):
        cells_to_birth = [(0, 0), (1, 1)]
        self.grid.birth_cells(cells_to_birth)
        self.assertEquals(self.grid.cells, set(cells_to_birth))
