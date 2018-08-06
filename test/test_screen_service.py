import unittest

from mock import MagicMock

from screen_service import ScreenService


class TestScreenService(unittest.TestCase):
    def setUp(self):
        self.mock_screen = MagicMock()

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

    def test__draw_border__should_draw_border(self):
        self.screen_service.draw_border()
        self.mock_screen.box.assert_called_once()
        self.mock_screen.refresh.assert_called_once()
