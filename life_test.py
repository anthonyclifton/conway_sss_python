import unittest

from life import Life

class TestLife(unittest.TestCase):
    def setUp(self):
        self.width = 5
        self.height = 4
        self.expected_cells = []

    def test_next__returns_blank_board_of_requested_dimensions_if_no_starting_items(self):
        life = Life([])
        cells = life.next()
        self.assertEqual(cells, self.expected_cells, 'Next() did not return a blank board.')

    def test_next__returns_blank_board_if_all_starting_cells_dead(self):
        life = Life([])
        cells = life.next()
        self.assertEqual(cells, self.expected_cells, 'Next() did not return a blank board.')

    def test_next__one_live_cell_with_two_live_neighbors_lives(self):
        starting_cells = [(1,1), (1,2), (1,3)]
        life = Life(starting_cells)
        cells = life.next()
        self.assertIn((1,2), cells, 'Board[1][2] was not alive.')

    def test_next__one_live_cell_with_three_live_neighbors_lives(self):
        starting_cells = [(1,1), (1,2), (1,3), (2,2)]
        life = Life(starting_cells)
        cells = life.next()
        self.assertIn((1,2), cells, 'Board[1][2] was not alive.')

    def test_next__one_live_cell_with_one_live_neighbors_dies(self):
        starting_cells = [(1,1), (1,2)]
        life = Life(starting_cells)
        cells = life.next()
        self.assertNotIn((1,2), cells, 'Board[1][2] was not dead.')

    def test_next__one_live_cell_with_zero_live_neighbors_dies(self):
        starting_cells = [(1,1)]
        life = Life(starting_cells)
        cells = life.next()
        self.assertNotIn((1,1), cells, 'Board[1][1] was not dead.')

    def test_next__one_dead_cell_with_three_live_neighbors_lives(self):
        starting_cells = [(1,1), (1,2), (1,3)]
        life = Life(starting_cells)
        cells = life.next()
        self.assertIn((2,2), cells, 'Board[2][2] was not alive.')

    def test_next__called_twice_block_of_four_living_all_stay_alive(self):
        starting_cells = [(1,1), (1,2), (2,1), (2,2)]
        life = Life(starting_cells)
        cells =life.next()
        cells = life.next()
        self.assertIn((1,1), cells, 'Board[1][1] was not alive.')
        self.assertIn((1,2), cells, 'Board[1][2] was not alive.')
        self.assertIn((2,1), cells, 'Board[2][1] was not alive.')
        self.assertIn((2,2), cells, 'Board[2][2] was not alive.')

    def test_next__preserves_the_beacon_oscillation(self):
        height = 6
        width = 6
        starting_cells = [(1,1), (1,2), (2,1), (2,2), (3,3), (3,4), (4,3), (4,4)]
        life = Life(starting_cells)

        cells = life.next()
        expected_board = [
                [0,0,0,0,0,0],
                [0,1,1,0,0,0],
                [0,1,0,0,0,0],
                [0,0,0,0,1,0],
                [0,0,0,1,1,0],
                [0,0,0,0,0,0]]
        self.assertIn((1,1), cells, 'Board[1][1] was not alive.')
        self.assertIn((1,2), cells, 'Board[1][2] was not alive.')
        self.assertIn((2,1), cells, 'Board[2][1] was not alive.')
        self.assertIn((3,4), cells, 'Board[3][4] was not alive.')
        self.assertIn((4,3), cells, 'Board[4][3] was not alive.')
        self.assertIn((4,4), cells, 'Board[4][4] was not alive.')

        cells = life.next()
        expected_board = [
                [0,0,0,0,0,0],
                [0,1,1,0,0,0],
                [0,1,1,0,0,0],
                [0,0,0,1,1,0],
                [0,0,0,1,1,0],
                [0,0,0,0,0,0]]
        self.assertIn((1,1), cells, 'Board[1][1] was not alive.')
        self.assertIn((1,2), cells, 'Board[1][2] was not alive.')
        self.assertIn((2,1), cells, 'Board[2][1] was not alive.')
        self.assertIn((3,4), cells, 'Board[3][4] was not alive.')
        self.assertIn((4,3), cells, 'Board[4][3] was not alive.')
        self.assertIn((4,4), cells, 'Board[4][4] was not alive.')

if __name__ == '__main__':
    unittest.main()
