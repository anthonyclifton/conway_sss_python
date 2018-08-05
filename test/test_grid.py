import unittest

from grid import Grid


class TestGrid(unittest.TestCase):
    def setUp(self):
        self.grid = Grid()

    def test__grid__should_birth_a_cell(self):
        expected_cell = (0, 0)
        self.grid.birth_cell(expected_cell)
        self.assertEquals(self.grid.cells[0], expected_cell)
