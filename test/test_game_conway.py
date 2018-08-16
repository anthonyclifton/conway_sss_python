import unittest

from mock import MagicMock

from game import Game
from grid import Grid


class TestGameConway(unittest.TestCase):
    def setUp(self):
        self.mock_screen_service = MagicMock()
        self.mock_screen_service.get_dimensions.return_value = (4, 4)

        self.mock_file_service = MagicMock()

        self.grid = Grid()
        self.game = Game(self.mock_screen_service,
                         self.mock_file_service,
                         self.grid)

        # lonely cells die (alive, less than 2 neighbors)
        # happy cells live (alive, 2 or 3 neighbors)
        # crowded cells die (alive, more than 3 neighbors)
        # new cells appear (dead, exactly 3 neighbors)

        # The tests in this suite are in a classicist style
        # where we are manipulating both the Unit Under Test
        # and a dependency that is not a test double.  Notice
        # that we are verifying state rather than behavior which
        # is more common in the mockist style.

    def test__update__should_kill_lonely_cells_with_zero_neighbors(self):
        self.grid.birth_cell((0, 0))
        self.game.update()
        self.assertEquals(len(self.grid.get_cells()), 0)

    def test__update__should_kill_lonely_cells_with_one_neighbor(self):
        self.grid.birth_cell((0, 0))
        self.grid.birth_cell((0, 1))
        self.game.update()
        self.assertEquals(len(self.grid.get_cells()), 0)

    def test__update__should_not_kill_happy_cells_with_two_neighbors(self):
        self.grid.birth_cell((0, 0))
        self.grid.birth_cell((1, 1))
        self.grid.birth_cell((2, 2))
        self.game.update()
        self.assertEquals(len(self.grid.get_cells()), 1)
        assert (1, 1) in self.grid.get_cells()

    def test__update__should_not_kill_happy_cells_with_three_neighbors(self):
        self.grid.birth_cell((0, 0))
        self.grid.birth_cell((0, 2))
        self.grid.birth_cell((-1, 1))
        self.grid.birth_cell((-2, 2))

        expected_cells = {(0, 1), (-1, 1), (-1, 2)}

        self.game.update()

        self.assertEquals(expected_cells, self.grid.get_cells())

    def test__update__should_kill_crowded_cells_with_more_than_three_neighbors(self):
        self.grid.birth_cell((0, 0))
        self.grid.birth_cell((0, 2))
        self.grid.birth_cell((-1, 1))
        self.grid.birth_cell((-2, 0))
        self.grid.birth_cell((-2, 2))

        expected_cells = {(0, 1), (-1, 0), (-1, 2), (-2, 1)}

        self.game.update()

        self.assertEquals(expected_cells, self.grid.get_cells())

    def test__update__should_birth_cells_when_they_would_have_three_neighbors(self):
        self.grid.birth_cell((0, 0))
        self.grid.birth_cell((0, 2))
        self.grid.birth_cell((-2, 2))
        self.game.update()
        self.assertEquals(len(self.grid.cells), 1)
        assert (-1, 1) in self.grid.get_cells()

    def test__update__should_handle_simple_oscillator(self):
        self.grid.birth_cell((0, 0))
        self.grid.birth_cell((0, 1))
        self.grid.birth_cell((0, 2))

        expected_cells_first_update = {(1, 1), (0, 1), (-1, 1)}
        self.game.update()
        self.assertEquals(expected_cells_first_update, self.grid.get_cells())

        expected_cells_second_update = {(0, 0), (0, 1), (0, 2)}
        self.game.update()
        self.assertEquals(expected_cells_second_update, self.grid.get_cells())
