import unittest

from mock import MagicMock

from game import Game
from grid import Grid


class TestConwayGame(unittest.TestCase):
    def setUp(self):
        self.grid = Grid()
        mock_screen_service = MagicMock()
        mock_screen_service.get_dimensions.return_value = (1, 1)
        self.game = Game(mock_screen_service, self.grid)

    def test__update__should_return_empty_list_when_all_cells_are_dead(self):
        self.grid.cells = {}
        result = self.game.update()
        self.assertEqual(0, len(result))

    def test__update__should_return_one_live_cell_when_only_one_can_live(self):
        self.grid.cells = {(0, 0), (1, 1), (2, 2)}
        result = self.game.update()
        self.assertEqual(1, len(result))
        assert (1, 1) in result

    def test__update__should_return_another_live_cell_when_only_one_can_live(self):
        self.grid.cells = {(1, 1), (2, 2), (3, 3)}
        result = self.game.update()
        self.assertEqual(1, len(result))
        assert (2, 2) in result

