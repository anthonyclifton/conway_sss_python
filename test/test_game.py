import unittest

from mock import MagicMock, call, patch
from game import Game
from grid import Grid


class TestGame(unittest.TestCase):
    def setUp(self):
        self.mock_screen_service = MagicMock()
        self.mock_file_service = MagicMock()
        self.mock_screen_service.get_dimensions.return_value = (4, 4)
        self.game = Game(self.mock_screen_service,
                         self.mock_file_service,
                         Grid())

    def test__init__should_create_fresh_grid(self):
        self.assertIsInstance(self.game.grid, Grid)

    def test__init__should_store_screen_service(self):
        self.assertEquals(self.game.screen_service, self.mock_screen_service)

    def test__init__should_store_game_start_timestamp(self):
        self.assertIsNotNone(self.game.start_timestamp)

    def test__display__should_draw_cells_on_screen(self):
        expected_cells = [(0, 0), (1, 1), (2, 2)]
        self.game.grid.cells.update(set(expected_cells))
        self.game.display([])
        calls = [call(expected_cells)]
        self.mock_screen_service.draw_cells.assert_has_calls(calls)

    def test__update__should_increment_generation_count(self):
        self.assertEquals(self.game.generation_count, 0)
        self.game.update()
        self.assertEquals(self.game.generation_count, 1)

    def test__update__should_display_status(self):
        self.game.update()
        self.mock_screen_service.draw_status.assert_called_once()

    @patch('game.time.sleep')
    def test__start__should_setup_border_and_gui(self, mock_sleep):
        fake_screen_service = FakeScreenService(1)
        mock_file_service = MagicMock()
        game = Game(fake_screen_service, mock_file_service, Grid())

        game.start()

        self.assertEquals(fake_screen_service.drew_ui, True)

    @patch('game.time.sleep')
    def test__start__should_start_game_loop(self, mock_sleep):
        fake_screen_service = FakeScreenService()
        mock_file_service = MagicMock()
        game = Game(fake_screen_service, mock_file_service, Grid())

        game.start()

        self.assertEquals(game.generation_count, fake_screen_service.draw_status_calls)
        self.assertEquals(game.generation_count, fake_screen_service.draw_cells_calls)
        self.assertEquals(game.generation_count, fake_screen_service.clear_cells_calls)

        self.assertEquals(game.generation_count, fake_screen_service.check_inputs_calls)
        self.assertEquals(1, fake_screen_service.cleanup_calls)

    @patch('game.time.sleep')
    def test__start__should_run_at_specified_rate(self, mock_sleep):
        fake_screen_service = FakeScreenService(3)
        mock_file_service = MagicMock()
        game = Game(fake_screen_service, mock_file_service, Grid())

        sleep_time = 0.123
        game.start(None, sleep_time)

        calls = [call(sleep_time), call(sleep_time), call(sleep_time)]
        mock_sleep.assert_has_calls(calls)

    @patch('game.time.sleep')
    def test__start__should_load_cell_file_when_provided(self, mock_sleep):
        expected_filename = 'test.csv'
        expected_cells = [(0, 0), (0, 1), (0, 2)]

        fake_screen_service = FakeScreenService(1)
        fake_file_service = FakeFileService(expected_filename, expected_cells)
        grid = Grid()
        game = Game(fake_screen_service, fake_file_service, grid)

        game.start(expected_filename)

        expected_cells_after_update = [(1, 1), (0, 1), (-1, 1)]

        self.assertEqual(set(expected_cells_after_update), grid.get_cells())


class FakeFileService(object):
    def __init__(self, expected_filename, expected_cells):
        self.expected_filename = expected_filename
        self.expected_cells = expected_cells
        self.actual_filename = None

    def read_cells(self, filename):
        self.actual_filename = filename
        if self.actual_filename == self.expected_filename:
            return self.expected_cells
        return []


class FakeScreenService(object):
    def __init__(self, allowed_loops=10):
        self.draw_status_calls = 0
        self.draw_cells_calls = 0
        self.clear_cells_calls = 0
        self.check_inputs_calls = 0
        self.cleanup_calls = 0
        self.allowed_loops = allowed_loops

        self.drew_ui = False

    def check_inputs(self):
        self.check_inputs_calls = self.check_inputs_calls + 1
        if self.draw_cells_calls == self.allowed_loops:
            return 0
        return 1

    def cleanup(self):
        self.cleanup_calls = self.cleanup_calls + 1

    @staticmethod
    def get_dimensions():
        return 10, 10

    def draw_ui(self):
        self.drew_ui = True

    def draw_status(self, generation_count, generations_per_second, living_cells):
        self.draw_status_calls = self.draw_status_calls + 1

    def draw_cells(self, cells):
        self.draw_cells_calls = self.draw_cells_calls + 1

    def clear_cells(self, cells):
        self.clear_cells_calls = self.clear_cells_calls + 1
