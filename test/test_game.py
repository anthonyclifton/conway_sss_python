import unittest

from mock import MagicMock, call
from game import Game
from grid import Grid


class TestGame(unittest.TestCase):
    def setUp(self):
        self.mock_screen_service = MagicMock()
        self.mock_screen_service.get_dimensions.return_value = (4, 4)
        self.game = Game(self.mock_screen_service)

    def test__init__should_create_fresh_grid(self):
        self.assertIsInstance(self.game.grid, Grid)

    def test__init__should_store_screen_service(self):
        self.assertEquals(self.game.screen_service, self.mock_screen_service)

    def test__init__should_store_game_start_timestamp(self):
        self.assertIsNotNone(self.game.start_timestamp)

    def test__update__should_add_new_random_cell(self):
        self.assertEquals(len(self.game.grid.cells), 0)
        self.game.update()
        self.assertEquals(len(self.game.grid.cells), 1)

    def test__update__should_remove_old_cell_when_adding_new(self):
        self.game.update()
        self.game.update()
        self.assertEquals(len(self.game.grid.cells), 1)

    def test__display__should_draw_cells_on_screen(self):
        expected_cells = [(0, 0), (1, 1), (2, 2)]
        self.game.grid.cells.update(set(expected_cells))
        self.game.display()
        calls = [call(expected_cells)]
        self.mock_screen_service.draw_cells.assert_has_calls(calls)

    def test__update__should_clear_dead_cell_from_screen(self):
        self.game.update()
        first_cell = list(self.game.grid.cells)[0]
        self.game.update()
        self.game.display()
        calls = [call([first_cell])]
        self.mock_screen_service.clear_cells.assert_has_calls(calls)

    def test__update__should_increment_generation_count(self):
        self.assertEquals(self.game.generation_count, 0)
        self.game.update()
        self.assertEquals(self.game.generation_count, 1)

    def test__update__should_display_status(self):
        self.game.update()
        self.mock_screen_service.draw_status.assert_called_once()

    def test__setup__should_setup_border_and_gui(self):
        self.game.setup()
        self.mock_screen_service.draw_ui.assert_called_once()

    def test__start__should_start_game_loop(self):
        fake_screen_service = FakeScreenService()
        game = Game(fake_screen_service)

        game.start()

        self.assertEquals(game.generation_count, fake_screen_service.draw_status_calls)
        self.assertEquals(game.generation_count, fake_screen_service.draw_cells_calls)
        self.assertEquals(game.generation_count, fake_screen_service.clear_cells_calls)


class FakeScreenService(object):
    def __init__(self):
        self.draw_status_calls = 0
        self.draw_cells_calls = 0
        self.clear_cells_calls = 0

    def check_inputs(self):
        if self.draw_cells_calls > 10:
            return 0
        return 1

    def cleanup(self):
        pass

    @staticmethod
    def get_dimensions():
        return 10, 10

    def draw_status(self, generation_count, generations_per_second, living_cells):
        self.draw_status_calls = self.draw_status_calls + 1

    def draw_cells(self, cells):
        self.draw_cells_calls = self.draw_cells_calls + 1

    def clear_cells(self, cells):
        self.clear_cells_calls = self.clear_cells_calls + 1
