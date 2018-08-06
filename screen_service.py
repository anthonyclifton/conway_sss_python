
class ScreenService(object):
    def __init__(self, curses):
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()

        # screen = self.stdscr.subwin(23, 79, 0, 0)
        # screen.box()
        # screen.refresh()
