from constants import GENERATION_LABEL_POSITION, GENERATION_LABEL, \
    GENERATIONS_PER_SECOND_LABEL_POSITION, \
    GENERATIONS_PER_SECOND_LABEL, LIVING_CELLS_LABEL_POSITION, \
    LIVING_CELLS_LABEL, GENERATION_VALUE_POSITION, \
    GENERATIONS_PER_SECOND_VALUE_POSITION, LIVING_CELLS_VALUE_POSITION, \
    UPPER_CASE_Q_KEY, LOWER_CASE_Q_KEY


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
        if c in [UPPER_CASE_Q_KEY, LOWER_CASE_Q_KEY]:
            return False
        return True

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
        self.draw_ui()

    def draw_ui(self):
        self.screen.box()
        self.screen.hline(2, 1, '_', self.width - 2)

        self.screen.addstr(GENERATION_LABEL_POSITION[0],
                           GENERATION_LABEL_POSITION[1],
                           GENERATION_LABEL)

        self.screen.addstr(GENERATIONS_PER_SECOND_LABEL_POSITION[0],
                           GENERATIONS_PER_SECOND_LABEL_POSITION[1],
                           GENERATIONS_PER_SECOND_LABEL)

        self.screen.addstr(LIVING_CELLS_LABEL_POSITION[0],
                           LIVING_CELLS_LABEL_POSITION[1],
                           LIVING_CELLS_LABEL)

        self.screen.refresh()

    def draw_status(self,
                    generation_count,
                    generations_per_second,
                    living_cells):

        self.screen.addstr(GENERATION_VALUE_POSITION[0],
                           GENERATION_VALUE_POSITION[1],
                           str(generation_count))

        self.screen.addstr(GENERATIONS_PER_SECOND_VALUE_POSITION[0],
                           GENERATIONS_PER_SECOND_VALUE_POSITION[1],
                           str(generations_per_second))

        self.screen.addstr(LIVING_CELLS_VALUE_POSITION[0],
                           LIVING_CELLS_VALUE_POSITION[1],
                           str(living_cells))

        self.screen.refresh()

    def draw_cells(self, cells):
        for cell in cells:
            y, x = cell
            if self.is_on_screen(x, y):
                self.screen.addch(y, x, 'O')
        self.screen.refresh()

    def clear_cells(self, cells):
        for cell in cells:
            y, x = cell
            if self.is_on_screen(x, y):
                self.screen.addch(y, x, ' ')
        self.screen.refresh()

    def cleanup(self):
        self.screen.erase()
        self.stdscr.keypad(0)
        self.curses.echo()
        self.curses.nocbreak()
        self.curses.curs_set(1)
        self.curses.endwin()

    def is_on_screen(self, x, y):
        return 0 < y < self.height - 1 and 0 < x < self.width - 1

    def get_dimensions(self):
        return self.height, self.width
