import unittest

from file_service import FileService


class TestFileService(unittest.TestCase):
    def setUp(self):
        self.file_service = FileService()

    def test__read_cells__should_return_list_of_cells_from_csv_file(self):
        filename = '../patterns/test.csv'

        expected_cells = [(3, 4), (3, 6), (4, 5), (5, 4), (5, 6)]

        actual_cells = self.file_service.read_cells(filename)

        self.assertEqual(expected_cells, actual_cells)

    def test__read_cells_from_lexicon_format__should_return_list_of_cells(self):
        filename = '../patterns/test.lex'

        expected_cells = [(3, 4), (3, 6), (4, 5), (5, 4), (5, 6)]

        actual_cells = self.file_service.read_cells_from_lexicon_format(filename)

        self.assertEqual(expected_cells, actual_cells)

