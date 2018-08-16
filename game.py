import time
from random import randint

from grid import Grid
from life import Life


class Game(object):
    def __init__(self, screen_service, grid):
        self.grid = grid
        self.screen_service = screen_service
        self.cells = []
        self.generation_count = 0
        self.start_timestamp = time.time()
        self.running = False
        self.life = Life()

    def setup(self):
        self.screen_service.draw_ui()

    def start(self):
        self.setup()
        self.running = True
        while self.running:
            time.sleep(0.5)
            self.update()

            if not self.screen_service.check_inputs():
                self.screen_service.cleanup()
                self.running = False

    def update(self):
        self.generation_count = self.generation_count + 1
        generations_per_second = int(self.generation_count / (time.time() - self.start_timestamp))

        self.screen_service.clear_cells(self.cells)
        self.cells = self.life.next()
        self.screen_service.draw_cells(self.cells)

        self.screen_service.draw_status(self.generation_count,
                                        generations_per_second,
                                        len(self.cells))


