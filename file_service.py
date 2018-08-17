from constants import ALIVE_CELL_CHARACTER


class FileService(object):
    def __init__(self):
        pass

    @staticmethod
    def read_cells(filename):
        # read from lexicon files from: http://www.conwaylife.com/ref/lexicon/lex.htm
        alive_cells = []
        cell_file = open(filename, 'r')

        for y, row in enumerate(cell_file):
            for x, cell in enumerate(list(row)):
                if cell == ALIVE_CELL_CHARACTER:
                    alive_cells.append((y, x))
        return alive_cells
