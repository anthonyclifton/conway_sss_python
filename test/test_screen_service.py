import unittest
from mock import MagicMock, call

from constants import GENERATION_LABEL_POSITION, GENERATION_LABEL, GENERATIONS_PER_SECOND_LABEL_POSITION, \
    GENERATIONS_PER_SECOND_LABEL, LIVING_CELLS_LABEL_POSITION, LIVING_CELLS_LABEL, GENERATION_VALUE_POSITION, \
    GENERATIONS_PER_SECOND_VALUE_POSITION, LIVING_CELLS_VALUE_POSITION
from screen_service import ScreenService

TEST_SCREEN_HEIGHT = 4
TEST_SCREEN_WIDTH = 4


class TestScreenService(unittest.TestCase):
    def setUp(self):
        self.mock_screen = MagicMock()
        self.mock_screen.getch.return_value = 10

        self.mock_stdscn = MagicMock()
        self.mock_stdscn.subwin.return_value = self.mock_screen
        self.mock_stdscn.getmaxyx.return_value = (TEST_SCREEN_HEIGHT, TEST_SCREEN_WIDTH)

        self.mock_curses = MagicMock()
        self.mock_curses.initscr.return_value = self.mock_stdscn

        self.screen_service = ScreenService(self.mock_curses)

    def test__init__should_set_up_curses_screen(self):
        self.mock_curses.initscr.assert_called_once()
        self.mock_curses.noecho.assert_called_once()
        self.mock_curses.cbreak.assert_called_once()
        self.mock_curses.curs_set.assert_called_once_with(0)
        self.mock_stdscn.subwin.assert_called_once_with(
            TEST_SCREEN_HEIGHT, TEST_SCREEN_WIDTH, 0, 0)
        self.mock_stdscn.keypad.assert_called_once_with(1)
        self.mock_stdscn.getmaxyx.assert_called_once()
        self.mock_screen.nodelay.assert_called_once_with(1)
        self.assertEquals(self.screen_service.height, 4)
        self.assertEquals(self.screen_service.width, 4)

    def test__get_dimensions__should_return_screen_dimensions(self):
        dimensions = self.screen_service.get_dimensions()
        self.assertEquals(dimensions, (4, 4))

    def test__draw_ui__should_draw_border(self):
        self.screen_service.draw_ui()

        self.mock_screen.box.assert_called_once()
        self.mock_screen.hline.assert_called_once()

        calls = [
            call(GENERATION_LABEL_POSITION[0],
                 GENERATION_LABEL_POSITION[1],
                 GENERATION_LABEL),
            call(GENERATIONS_PER_SECOND_LABEL_POSITION[0],
                 GENERATIONS_PER_SECOND_LABEL_POSITION[1],
                 GENERATIONS_PER_SECOND_LABEL),
            call(LIVING_CELLS_LABEL_POSITION[0],
                 LIVING_CELLS_LABEL_POSITION[1],
                 LIVING_CELLS_LABEL)
        ]

        self.mock_screen.addstr.assert_has_calls(calls)

        self.mock_screen.refresh.assert_called_once()

    def test__draw_cells__should_draw_cells_when_given_a_list_of_tuples(self):
        self.screen_service.height = 5
        self.screen_service.width = 5

        cells = [(1, 1), (2, 2), (3, 3)]

        self.screen_service.draw_cells(cells)

        calls = [call(1, 1, 'O'), call(2, 2, 'O'), call(3, 3, 'O')]

        self.mock_screen.addch.assert_has_calls(calls)
        self.mock_screen.refresh.assert_called_once()

    def test__draw_status__should_draw_status_on_status_line(self):
        expected_generation_count = str(123)
        expected_generations_per_second = str(12.3)
        expected_living_cells = str(45)

        self.screen_service.draw_status(expected_generation_count,
                                        expected_generations_per_second,
                                        expected_living_cells)

        calls = [
            call(GENERATION_VALUE_POSITION[0],
                 GENERATION_VALUE_POSITION[1],
                 expected_generation_count),
            call(GENERATIONS_PER_SECOND_VALUE_POSITION[0],
                 GENERATIONS_PER_SECOND_VALUE_POSITION[1],
                 expected_generations_per_second),
            call(LIVING_CELLS_VALUE_POSITION[0],
                 LIVING_CELLS_VALUE_POSITION[1],
                 expected_living_cells)

        ]

        self.mock_screen.addstr.assert_has_calls(calls)
        self.mock_screen.refresh.assert_called_once()

    def test__clear_cells__should_clear_cells_when_given_a_list_of_tuples(self):
        self.screen_service.height = 5
        self.screen_service.width = 5

        cells = [(1, 1), (2, 2), (3, 3)]

        self.screen_service.clear_cells(cells)

        calls = [call(1, 1, ' '), call(2, 2, ' '), call(3, 3, ' ')]

        self.mock_screen.addch.assert_has_calls(calls)
        self.mock_screen.refresh.assert_called_once()

    def test__draw_cells__should_not_draw_tuple_that_is_off_the_screen(self):
        self.screen_service.height = 3
        self.screen_service.width = 3

        cells = [(0, 1), (1, 0), (2, 1), (1, 2), (10, 10), (-10, -10)]
        self.screen_service.draw_cells(cells)
        self.mock_screen.addch.assert_not_called()

    def test__clear_cells__should_not_clear_tuple_that_is_off_the_screen(self):
        self.screen_service.height = 3
        self.screen_service.width = 3

        cells = [(0, 1), (1, 0), (2, 1), (1, 2), (10, 10), (-10, -10)]
        self.screen_service.clear_cells(cells)
        self.mock_screen.addch.assert_not_called()

    def test__cleanup__should_return_terminal_to_sane_state(self):
        self.screen_service.cleanup()

        calls = [call(1), call(0)]
        self.mock_stdscn.keypad.assert_has_calls(calls)
        self.mock_curses.echo.assert_called_once()
        self.mock_curses.nocbreak.assert_called_once()
        self.mock_curses.endwin.assert_called_once()

    def test__check_keyboard__should_return_zero_when_enter_key_pressed(self):
        key_pressed = self.screen_service.check_inputs()
        self.assertEquals(key_pressed, 0)

    def test__handle_terminal_resize__should_update_screen(self):
        self.screen_service.handle_terminal_resize()

        self.assertEquals(self.screen_service.height, 4)
        self.assertEquals(self.screen_service.width, 4)
        self.assertEquals(self.mock_stdscn.subwin.call_count, 2)

        self.assertEquals(self.mock_screen.nodelay.call_count, 2)
        self.assertEquals(self.mock_screen.erase.call_count, 1)
        self.assertEquals(self.mock_screen.refresh.call_count, 2)
