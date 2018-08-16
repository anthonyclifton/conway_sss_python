import curses

from constants import CELL_FILE, SLEEP_PER_UPDATE
from file_service import FileService
from game import Game
from grid import Grid
from screen_service import ScreenService

screen_service = ScreenService(curses)
file_service = FileService()
grid = Grid()
game = Game(screen_service, file_service, grid)

if __name__ == '__main__':
    game.start(CELL_FILE, SLEEP_PER_UPDATE)

