import curses

from game import Game
from grid import Grid
from screen_service import ScreenService

screen_service = ScreenService(curses)
grid = Grid()
game = Game(screen_service, grid)

if __name__ == '__main__':
    game.start()

