import unittest

from mock import MagicMock

# from game import Game

# lonely cells die (alive, less than 2 neighbors)
# happy cells live (alive, 2 or 3 neighbors)
# crowded cells die (alive, more than 3 neighbors)
# new cells appear (dead, 3 neighbors or more)
# from grid import Grid


class TestGameConway(unittest.TestCase):
    def setUp(self):
        self.mock_screen_service = MagicMock()
        self.mock_screen_service.get_dimensions.return_value = (4, 4)

    def test__update__should_kill_lonely_cells(self):
        # grid = Grid()
        # game = Game(self.mock_screen_service, grid)
        # grid.cells = {(0, 0)}
        # game.update()
        # self.assertEquals(len(grid.cells), 0)
        pass
