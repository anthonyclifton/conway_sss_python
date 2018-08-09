from random import randint

from grid import Grid


class Game(object):
    def __init__(self, screen_service):
        self.grid = Grid()
        self.screen_service = screen_service

    def update(self):
        if len(self.grid.cells) > 0:
            self.grid.kill_cell(list(self.grid.cells)[0])
        random_cell = (randint(0, 9), randint(0, 9))
        self.grid.birth_cell(random_cell)

    def display(self):
        self.screen_service.draw(list(self.grid.cells))
