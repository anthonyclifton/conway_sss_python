import curses
from time import sleep

from screen_service import ScreenService

screen_service = ScreenService(curses)

if __name__ == '__main__':
    while True:
        sleep(100)
