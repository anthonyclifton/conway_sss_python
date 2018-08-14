class ScreenService(object):
    def __init__(self, curses):
        self.curses = curses
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        self.stdscr.keypad(1)
        self.height, self.width = self.stdscr.getmaxyx()
        self.screen = self.stdscr.subwin(
            self.height,
            self.width,
            0,
            0)
        self.screen.nodelay(1)

    def check_inputs(self):
        c = self.screen.getch()
        if c == self.curses.KEY_RESIZE:
            self.handle_terminal_resize()
        if c == 10:
            return 0
        return 1

    def handle_terminal_resize(self):
        self.height, self.width = self.stdscr.getmaxyx()
        self.screen = self.stdscr.subwin(
            self.height - 1,
            self.width - 1,
            0,
            0)
        self.screen.nodelay(1)
        self.screen.erase()
        self.screen.refresh()
        self.draw_border()

    def draw_border(self):
        self.screen.box()
        self.screen.refresh()

    def draw(self, cells):
        for cell in cells:
            y, x = cell
            if self.is_on_screen(x, y):
                self.screen.addch(y, x, 'O')
        self.screen.refresh()

    def clear(self, cells):
        for cell in cells:
            y, x = cell
            if self.is_on_screen(x, y):
                self.screen.addch(y, x, ' ')
        self.screen.refresh()

    def cleanup(self):
        # todo clear the screen
        self.stdscr.keypad(0)
        self.curses.echo()
        self.curses.nocbreak()
        self.curses.endwin()

    def is_on_screen(self, x, y):
        return 0 < y < self.height - 1 and 0 < x < self.width - 1

    def get_dimensions(self):
        return self.height, self.width
