
class ScreenService(object):
    def __init__(self, curses):
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.screen = self.stdscr.subwin(23, 79, 0, 0)

    def draw_border(self):
        self.screen.box()
        self.screen.refresh()
