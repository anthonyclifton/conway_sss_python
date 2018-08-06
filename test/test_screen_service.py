import curses
import unittest

from mock import MagicMock, call

from screen_service import ScreenService


class TestScreenService(unittest.TestCase):
    def setUp(self):
        self.mock_screen = MagicMock()
        self.mock_screen.getch.return_value = 10

        self.mock_stdscn = MagicMock()
        self.mock_stdscn.subwin.return_value = self.mock_screen

        self.mock_curses = MagicMock()
        self.mock_curses.initscr.return_value = self.mock_stdscn

        self.screen_service = ScreenService(self.mock_curses)

    def test__init__should_set_up_curses_screen(self):
        self.mock_curses.initscr.assert_called_once()
        self.mock_curses.noecho.assert_called_once()
        self.mock_curses.cbreak.assert_called_once()
        self.mock_stdscn.subwin.assert_called_once()
        self.mock_stdscn.keypad.assert_called_once_with(1)
        self.mock_screen.nodelay.assert_called_once_with(1)

    def test__draw_border__should_draw_border(self):
        self.screen_service.draw_border()

        self.mock_screen.box.assert_called_once()
        self.mock_screen.refresh.assert_called_once()

    def test__cleanup__should_return_terminal_to_sane_state(self):
        self.screen_service.cleanup()

        calls = [call(1), call(0)]
        self.mock_stdscn.keypad.assert_has_calls(calls)
        self.mock_curses.echo.assert_called_once()
        self.mock_curses.nocbreak.assert_called_once()
        self.mock_curses.endwin.assert_called_once()

    def test__check_keyboard__should_return_zero_when_enter_key_pressed(self):
        key_pressed = self.screen_service.check_keyboard()
        self.assertEquals(key_pressed, 0)
