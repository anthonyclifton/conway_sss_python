import time


class Game(object):
    def __init__(self, screen_service, file_service, grid):
        self.grid = grid
        self.screen_service = screen_service
        self.file_service = file_service
        self.generation_count = 0
        self.start_timestamp = time.time()
        self.running = False

    def start(self, cell_filename=None, sleep_time=0.1):
        self._setup(self.screen_service)

        if cell_filename:
            loaded_cells = self.file_service.read_cells(cell_filename)
            self.grid.birth_cells(loaded_cells)

        self.running = True
        while self.running:
            time.sleep(sleep_time)
            new_cells, dead_cells = self.update()
            self.display(dead_cells)

            if not self.screen_service.check_inputs():
                self.screen_service.cleanup()
                self.running = False

    def update(self):
        self.generation_count = self.generation_count + 1
        generations_per_second = int(self.generation_count / (time.time() - self.start_timestamp))
        self.screen_service.draw_status(self.generation_count,
                                        generations_per_second,
                                        len(self.grid.cells))

        new_cells = self._find_new_cells(self.grid)
        dead_cells = self._find_dying_cells(self.grid)

        self._add_new_cells(self.grid, new_cells)
        self._remove_dead_cells(self.grid, dead_cells)

        return new_cells, dead_cells

    def display(self, dead_cells):
        self.screen_service.clear_cells(dead_cells)
        self.screen_service.draw_cells(list(self.grid.get_cells()))

    @staticmethod
    def _setup(screen_service):
        screen_service.draw_ui()

    @staticmethod
    def _find_new_cells(grid):
        new_cells = set()
        for cell in grid.get_cells():
            empty_neighbors = grid.get_adjacent_empty_cells(cell)
            birthing_cells = [possible for possible in empty_neighbors
                              if grid.count_neighbors(possible) == 3]
            new_cells.update(birthing_cells)
        return list(new_cells)

    @staticmethod
    def _find_dying_cells(grid):
        dying_cells = set()
        for cell in grid.get_cells():
            neighbors = grid.count_neighbors(cell)

            if neighbors < 2 or neighbors > 3:
                dying_cells.add(cell)
        return list(dying_cells)

    @staticmethod
    def _add_new_cells(grid, new_cells):
        for new_cell in new_cells:
            grid.birth_cell(new_cell)

    @staticmethod
    def _remove_dead_cells(grid, dead_cells):
        for dead_cell in dead_cells:
            grid.kill_cell(dead_cell)
