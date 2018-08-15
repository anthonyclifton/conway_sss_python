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

    def test__birth_cells__should_set_cells(self):
        cells_to_birth = [(0, 0), (1, 1)]
        self.grid.birth_cells(cells_to_birth)
        self.assertEquals(self.grid.get_cells(), set(cells_to_birth))

    def test__get_cells__should_return_current_cells(self):
        cells_to_birth = [(0, 0), (1, 1)]
        self.grid.birth_cells(cells_to_birth)
        cells = self.grid.get_cells()
        self.assertEquals(cells, set(cells_to_birth))

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

    def test__count_neighbors__should_return_just_one_when_non_adjacent_cells_alive(self):
        self.grid.cells = {
            (0, 0), (0, 1), (0, 2)
        }

        neighbors_count = self.grid.count_neighbors((0, 0))
        self.assertEquals(neighbors_count, 1)

    def test__count_neighbors__should_return_zero_when_non_adjacent_cells_alive(self):
        self.grid.cells = {
            (0, 0), (1, 2)
        }

        neighbors_count = self.grid.count_neighbors((0, 0))
        self.assertEquals(neighbors_count, 0)

    def test__count_neighbors__should_return_four_when_chuckwagon_configuration(self):
        self.grid.cells = {
            (0, 0), (0, 2),
            (1, 1),
            (2, 0), (2, 2)
        }

        neighbors_count = self.grid.count_neighbors((1, 1))
        self.assertEquals(neighbors_count, 4)

    def test__get_adjacent_empty_cells__should_return_list_of_empty_adjacent_cells(self):
        self.grid.cells = {(0, 0)}

        expected_adjacent_empty_cells = [
            (1, -1), (1, 0), (1, 1),
            (0, -1), (0, 1),
            (-1, -1), (-1, 0), (-1, 1)
        ]

        actual_adjacent_empty_cells = self.grid.get_adjacent_empty_cells((0, 0))

        self.assertEquals(len(actual_adjacent_empty_cells), 8)
        self.assertEquals(set(actual_adjacent_empty_cells), set(expected_adjacent_empty_cells))

    def test__get_adjacent_empty_cells__should_return_list_of_empties_minus_alives(self):
        self.grid.cells = {
            (1, 0),
            (0, -1), (0, 1),
            (-1, 0),
        }

        expected_adjacent_empty_cells = [
            (1, -1), (1, 1),
            (-1, -1), (-1, 1)
        ]

        actual_adjacent_empty_cells = self.grid.get_adjacent_empty_cells((0, 0))

        self.assertEquals(len(actual_adjacent_empty_cells), 4)
        self.assertEquals(set(actual_adjacent_empty_cells), set(expected_adjacent_empty_cells))
