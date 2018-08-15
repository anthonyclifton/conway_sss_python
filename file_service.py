import csv

from constants import ALIVE_CELL_CHARACTER


class FileService(object):
    def __init__(self):
        pass

    @staticmethod
    def read_cells(filename):
        alive_cells = []
        with open(filename, 'rb') as cell_file:
            cell_file_reader = csv.reader(cell_file, delimiter=',', quotechar='|')

            for y, row in enumerate(cell_file_reader):
                for x, cell in enumerate(row):
                    if cell == ALIVE_CELL_CHARACTER:
                        alive_cells.append((y, x))
        return alive_cells
