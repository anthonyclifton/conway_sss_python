import time


class Game(object):
    def __init__(self, screen_service, file_service, grid):
        self.grid = grid
        self.screen_service = screen_service
        self.file_service = file_service
        self.generation_count = 0
        self.start_timestamp = time.time()
        self.running = False

    def start(self, filename=None, sleep_time=0.1):
        self._setup(self.screen_service)

        self._load_file_into_grid(self.file_service, self.grid, filename)

        self.running = True
        while self.running:
            time.sleep(sleep_time)
            new_cells, dead_cells = self.update()
            self.display(new_cells, dead_cells)

            if not self.screen_service.check_inputs():
                self.screen_service.cleanup()
                self.running = False

    def update(self):
        self.generation_count = self._update_status(self.screen_service,
                                                    self.grid,
                                                    self.generation_count,
                                                    self.start_timestamp)

        new_cells = self._find_new_cells(self.grid)
        dead_cells = self._find_dying_cells(self.grid)

        self.grid.birth_cells(new_cells)
        self.grid.kill_cells(dead_cells)

        return new_cells, dead_cells

    def display(self, new_cells, dead_cells):
        self.screen_service.clear_cells(dead_cells)
        self.screen_service.draw_cells(new_cells)

    @staticmethod
    def _update_status(screen_service, grid, generation_count, start_timestamp):
        generation_count = generation_count + 1
        generations_per_second = int(generation_count / (time.time() - start_timestamp))
        screen_service.draw_status(generation_count,
                                   generations_per_second,
                                   len(grid.get_cells()))
        return generation_count

    @staticmethod
    def _setup(screen_service):
        screen_service.draw_ui()

    @staticmethod
    def _load_file_into_grid(file_service, grid, filename):
        if filename:
            loaded_cells = file_service.read_cells(filename)
            grid.birth_cells(loaded_cells)

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

