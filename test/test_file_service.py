import unittest

from file_service import FileService


class TestFileService(unittest.TestCase):
    def setUp(self):
        self.file_service = FileService()

    def test__read_cells__should_return_list_of_cells_from_csv_file(self):
        filename = '../patterns/test.csv'

        expected_cells = [
            (0, 0), (0, 2),
            (1, 1),
            (2, 0), (2, 2)
        ]

        actual_cells = self.file_service.read_cells(filename)

        self.assertEqual(actual_cells, expected_cells)
