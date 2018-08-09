from random import randint

from grid import Grid


class Game(object):
    def __init__(self, screen_service):
        self.grid = Grid()
        self.screen_service = screen_service
        self.dead_cells = []

    def update(self):
        if len(self.grid.cells) > 0:
            cell_to_kill = list(self.grid.cells)[0]
            self.grid.kill_cell(cell_to_kill)
            self.dead_cells = [cell_to_kill]
        random_cell = (randint(1, 20), randint(1, 20))
        self.grid.birth_cell(random_cell)

    def display(self):
        self.screen_service.clear(self.dead_cells)
        self.screen_service.draw(list(self.grid.cells))
