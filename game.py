import time


class Game(object):
    def __init__(self, screen_service, file_service, grid):
        self.grid = grid
        self.screen_service = screen_service
        self.file_service = file_service
        self.dead_cells = []
        self.new_cells = []
        self.generation_count = 0
        self.start_timestamp = time.time()
        self.running = False

    def start(self, cell_filename=None, sleep_time=0.1):
        self._setup()

        if cell_filename:
            loaded_cells = self.file_service.read_cells(cell_filename)
            self.grid.birth_cells(loaded_cells)

        self.running = True
        while self.running:
            time.sleep(sleep_time)
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

        self.new_cells = self._find_new_cells()
        self.dead_cells = self._find_dying_cells()

        self._add_new_cells()
        self._remove_dead_cells()

    def display(self):
        self.screen_service.clear_cells(self.dead_cells)
        self.screen_service.draw_cells(list(self.grid.cells))

    def _setup(self):
        self.screen_service.draw_ui()

    def _find_new_cells(self):
        new_cells = set()
        for cell in self.grid.cells:
            empty_neighbors = self.grid.get_adjacent_empty_cells(cell)
            birthing_cells = [possible for possible in empty_neighbors
                              if self.grid.count_neighbors(possible) == 3]
            new_cells.update(birthing_cells)
        return list(new_cells)

    def _find_dying_cells(self):
        dying_cells = set()
        for cell in self.grid.cells:
            neighbors = self.grid.count_neighbors(cell)

            if neighbors < 2 or neighbors > 3:
                dying_cells.add(cell)
        return list(dying_cells)

    def _add_new_cells(self):
        for new_cell in self.new_cells:
            self.grid.birth_cell(new_cell)

    def _remove_dead_cells(self):
        for dead_cell in self.dead_cells:
            self.grid.kill_cell(dead_cell)
