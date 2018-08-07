from grid import Grid


class Game(object):
    def __init__(self, screen_service):
        self.grid = Grid()
        self.screen_service = screen_service
