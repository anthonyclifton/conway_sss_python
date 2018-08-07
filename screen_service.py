class ScreenService(object):
    def __init__(self, curses):
        self.curses = curses
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.stdscr.keypad(1)
        self.height, self.width = self.stdscr.getmaxyx()
        self.screen = self.stdscr.subwin(self.height - 1, self.width - 1, 0, 0)
        self.screen.nodelay(1)

    def check_keyboard(self):
        c = self.screen.getch()
        if c == 10:
            return 0
        return 1

    def draw_border(self):
        self.screen.box()
        self.screen.refresh()

    def cleanup(self):
        self.stdscr.keypad(0)
        self.curses.echo()
        self.curses.nocbreak()
        self.curses.endwin()
