import unittest

from mock import MagicMock

from game import Game
from grid import Grid


class TestGameConway(unittest.TestCase):
    def setUp(self):
        self.mock_screen_service = MagicMock()
        self.mock_screen_service.get_dimensions.return_value = (4, 4)

        self.grid = Grid()
        self.game = Game(self.mock_screen_service, self.grid)

        # lonely cells die (alive, less than 2 neighbors)
        # happy cells live (alive, 2 or 3 neighbors)
        # crowded cells die (alive, more than 3 neighbors)
        # new cells appear (dead, 3 neighbors or more)

        # The tests in this suite are in a classicist style
        # where we are manipulating both the Unit Under Test
        # and a dependency that is not a test double.  Notice
        # that we are verifying state rather than behavior which
        # is more common in the mockist style.

    def test__update__should_kill_lonely_cells_with_zero_neighbors(self):
        self.grid.birth_cell((0, 0))
        self.game.update()
        self.assertEquals(len(self.grid.cells), 0)

    def test__update__should_kill_lonely_cells_with_one_neighbor(self):
        self.grid.birth_cell((0, 0))
        self.grid.birth_cell((0, 1))
        self.game.update()
        self.assertEquals(len(self.grid.cells), 0)

    def test__update__should_not_kill_happy_cells_with_two_neighbors(self):
        self.grid.birth_cell((0, 0))
        self.grid.birth_cell((1, 1))
        self.grid.birth_cell((2, 2))
        self.game.update()
        self.assertEquals(len(self.grid.cells), 1)
        self.assertEquals(list(self.grid.cells)[0], (1, 1))

    def test__update__should_not_kill_happy_cells_with_three_neighbors(self):
        self.grid.birth_cell((0, 0))
        self.grid.birth_cell((0, 2))
        self.grid.birth_cell((-1, 1))
        self.grid.birth_cell((-2, 2))

        expected_cells = {
            (0, 1),
            (-1, 1), (-1, 2)
        }
        self.game.update()
        self.assertEquals(self.grid.cells, expected_cells)

    def test__update__should_kill_crowded_cells_with_more_than_three_neighbors(self):
        self.grid.birth_cell((0, 0))
        self.grid.birth_cell((0, 2))
        self.grid.birth_cell((-1, 1))
        self.grid.birth_cell((-2, 0))
        self.grid.birth_cell((-2, 2))

        expected_cells = {
            (0, 1),
            (-1, 0), (-1, 2),
            (-2, 1)
        }

        self.game.update()
        self.assertEquals(self.grid.cells, expected_cells)

    def test__update__should_birth_cells_when_they_would_have_three_neighbors(self):
        self.grid.birth_cell((0, 0))
        self.grid.birth_cell((0, 2))
        self.grid.birth_cell((-2, 2))
        self.game.update()
        self.assertEquals(len(self.grid.cells), 1)
        self.assertEquals(list(self.grid.cells)[0], (-1, 1))

    def test__update__should_birth_cells_when_they_would_have_more_than_three_neighbors(self):
        self.grid.birth_cell((0, 0))
        self.grid.birth_cell((0, 2))
        self.grid.birth_cell((-2, 0))
        self.grid.birth_cell((-2, 2))
        self.game.update()
        self.assertEquals(len(self.grid.cells), 1)
        self.assertEquals(list(self.grid.cells)[0], (-1, 1))

    def test__update__should_handle_simple_oscillator(self):
        pass
