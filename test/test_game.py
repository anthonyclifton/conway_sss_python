import unittest
from mock import MagicMock, call
from game import Game
from grid import Grid


class TestGame(unittest.TestCase):
    def setUp(self):
        self.mock_screen_service = MagicMock()
        self.game = Game(self.mock_screen_service)

    def test__init__should_create_fresh_grid(self):
        self.assertIsInstance(self.game.grid, Grid)

    def test__init__should_store_screen_service(self):
        self.assertEquals(self.game.screen_service, self.mock_screen_service)

    def test__update__should_add_new_random_cell(self):
        self.assertEquals(len(self.game.grid.cells), 0)
        self.game.update()
        self.assertEquals(len(self.game.grid.cells), 1)

    def test__update__should_remove_old_cell_when_adding_new(self):
        self.game.update()
        first_cell = list(self.game.grid.cells)[0]
        self.game.update()
        assert first_cell not in self.game.grid.cells
        self.assertEquals(len(self.game.grid.cells), 1)

    def test__display__should_draw_cells_on_screen(self):
        expected_cells = [(0, 0), (1, 1), (2, 2)]
        self.game.grid.cells.update(set(expected_cells))
        self.game.display()
        calls = [call(expected_cells)]
        self.mock_screen_service.draw.assert_has_calls(calls)

