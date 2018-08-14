import unittest

from mock import MagicMock

from game import Game

# lonely cells die (alive, less than 2 neighbors)
# happy cells live (alive, 2 or 3 neighbors)
# crowded cells die (alive, more than 3 neighbors)
# new cells appear (dead, 3 neighbors or more)


class TestGameConway(unittest.TestCase):
    def setUp(self):
        self.mock_screen_service = MagicMock()

    def test__update__should_kill_lonely_cells(self):
        game = Game(self.mock_screen_service)
        game.grid.cells = {(0, 0)}
