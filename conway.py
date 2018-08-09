import curses
from time import sleep

from game import Game
from screen_service import ScreenService

screen_service = ScreenService(curses)
game = Game(screen_service)

if __name__ == '__main__':
    screen_service.draw_border()
    running = True
    while running:
        sleep(0.1)
        if screen_service.check_keyboard() == 0:
            screen_service.cleanup()
            running = False

        game.update()
        game.display()

