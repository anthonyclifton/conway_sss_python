import curses

from game import Game
from screen_service import ScreenService

screen_service = ScreenService(curses)
game = Game(screen_service)

if __name__ == '__main__':
    game.setup()
    game.start()

