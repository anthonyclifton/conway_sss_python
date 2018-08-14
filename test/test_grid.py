import unittest
from grid import Grid


class TestGrid(unittest.TestCase):
    def setUp(self):
        self.grid = Grid()

    def tearDown(self):
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

    def test__count_neighbors__should_return_zero_when_no_neighbors(self):
        lonely_cell = (0, 0)
        self.grid.birth_cell(lonely_cell)
        neighbors_count = self.grid.count_neighbors(lonely_cell)
        self.assertEquals(neighbors_count, 0)

    def test__count_neighbors__should_return_one_when_one_neighbor(self):
        not_so_lonely_cell = (0, 0)
        neighborly_cell = (0, 1)
        self.grid.birth_cell(not_so_lonely_cell)
        self.grid.birth_cell(neighborly_cell)
        neighbors_count = self.grid.count_neighbors(not_so_lonely_cell)
        self.assertEquals(neighbors_count, 1)

    def test__count_neighbors__should_return_eight_when_all_adjacent_cells_alive(self):
        self.grid.cells = {
            (-1, 1), (0, 1), (1, 1),
            (-1, 0), (0, 0), (1, 0),
            (-1, -1), (0, -1), (1, -1)
        }

        neighbors_count = self.grid.count_neighbors((0, 0))
        self.assertEquals(neighbors_count, 8)

