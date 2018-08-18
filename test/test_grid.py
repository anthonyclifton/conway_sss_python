import unittest
from grid import Grid, Generation


class TestGrid(unittest.TestCase):
    def setUp(self):
        self.grid = Grid()

    def tearDown(self):
        self.grid = None

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

    def test__birth_cells__should_set_cells(self):
        cells_to_birth = [(0, 0), (1, 1)]
        self.grid.birth_cells(cells_to_birth)
        self.assertEquals(self.grid.get_cells(), set(cells_to_birth))

    def test__get_cells__should_return_current_cells(self):
        cells_to_birth = [(0, 0), (1, 1)]
        self.grid.birth_cells(cells_to_birth)
        cells = self.grid.get_cells()
        self.assertEquals(cells, set(cells_to_birth))

    def test__grid_given_empty_list__should_return_empty_cells(self):
        expected_cells = Generation()
        cells = self.grid.generate_next_generation()
        self.assertEquals(expected_cells, cells)

    def test__grid_cell_with_two_neighbors_survives(self):
        original_cells2 = [(0, 0), (1, 1), (2, 2)]
        expected_cells = Generation({(1, 1)}, {(0, 0), (2, 2)})
        self.grid.birth_cells(original_cells2)
        actual_cells = self.grid.generate_next_generation()
        self.assertEquals(expected_cells, actual_cells)

    def test__grid_cell_with_three_neighbors_survives(self):
        original_cells = [(0, 0), (1, 1), (2, 2), (2,0)]
        expected_cells = Generation({(1, 1)}, {(0, 0), (2, 2), (2, 0)})
        self.grid.birth_cells(original_cells)
        actual_cells = self.grid.generate_next_generation()
        self.assertEquals(expected_cells, actual_cells)
