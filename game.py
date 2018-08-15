import time
from random import randint


class Game(object):
    def __init__(self, screen_service, grid):
        self.grid = grid
        self.screen_service = screen_service
        self.dead_cells = []
        self.generation_count = 0
        self.start_timestamp = time.time()
        self.running = False

    def setup(self):
        self.screen_service.draw_ui()

    def start(self):
        self.setup()
        self.running = True
        while self.running:
            time.sleep(0.5)
            self.update()
            self.display()

            if not self.screen_service.check_inputs():
                self.screen_service.cleanup()
                self.running = False

    def update(self):
        self.generation_count = self.generation_count + 1
        generations_per_second = int(self.generation_count / (time.time() - self.start_timestamp))
        self.screen_service.draw_status(self.generation_count,
                                        generations_per_second,
                                        len(self.grid.cells))
        # if len(self.grid.cells) > 0:
        #     cell_to_kill = list(self.grid.cells)[0]
        #     self.grid.kill_cell(cell_to_kill)
        #     self.dead_cells = [cell_to_kill]
        #
        # screen_height, screen_width = self.screen_service.get_dimensions()
        # random_cell = (randint(0, screen_height),
        #                randint(0, screen_width))
        # self.grid.birth_cell(random_cell)
        self.dead_cells = []

        for cell in self.grid.cells:
            neighbors = self.grid.count_neighbors(cell)

            if neighbors < 2 or neighbors > 3:
                self.dead_cells.append(cell)

        self._remove_dead_cells()

    def display(self):
        self.screen_service.clear_cells(self.dead_cells)
        self.screen_service.draw_cells(list(self.grid.cells))

    def _remove_dead_cells(self):
        for dead_cell in self.dead_cells:
            self.grid.kill_cell(dead_cell)
