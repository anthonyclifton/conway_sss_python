import unittest

def crazy_conway(grid):
    falsed_grid = [[False for _ in range(len(grid[0]) + 2)] for _ in range(len(grid) + 2)]
    c = [[False] + row + [False] for row in grid]
    falsed_grid[1:-1] = c
    return [[two_live_neighbors_retains_life(live_neighbor_count(slice_it(falsed_grid, rowIndex + 1, columnIndex + 1))) for columnIndex in range(len(grid[0]))] for rowIndex in range(len(grid))]

def slice_it(grid, rowIndex, columnIndex):
    return [row[columnIndex - 1: columnIndex + 1] for row in grid[rowIndex - 1: rowIndex + 1]]

def two_live_neighbors_retains_life(count):
    #return bool(max(count - 1, 0))
    return count - 2 == 0 or count - 3 == 0

def live_neighbor_count(grid):
    return sum([sum(x) for x in grid]) - int(grid[1][1])

class TestCrazyConwayGame(unittest.TestCase):
    def setUp(self):
        pass

    def test__one_lonely_live_cell_dies_from_loneliness(self):
        grid = [[True]]

        tng = crazy_conway(grid)

        self.assertEqual([[False]], tng)

    def test__two_lonely_horizontal_cells_die_from_loneliness(self):
        grid = [[True, True]]

        tng = crazy_conway(grid)

        self.assertEqual([[False, False]], tng)

    def test__two_lonely_vertical_cells_die_from_loneliness(self):
        grid = [[True], [True]]

        tng = crazy_conway(grid)

        self.assertEqual([[False], [False]], tng)

    def test__one_lonely_cell_with_dead_neighbor_dies(self):
        grid = [[True], [False]]

        tng = crazy_conway(grid)

        self.assertEqual([[False], [False]], tng)

    def test__three_neighbors_spawn_new_friend(self):
        grid = [[True, False], [True, True]]

        tng = crazy_conway(grid)

        self.assertEqual([[True, True], [True, True]], tng)

    def test__tainted_puppy_chow_causes_much_death(self):
        grid = [
            [True, False, True],
            [False, False, False],
            [True, False, True],

        ]
        
        expected_grid = [
            [False, False, False],
            [False, False, False],
            [False, False, False],
        ]

        tng = crazy_conway(grid)

        self.assertEqual(expected_grid, tng)

    # def test__stuff_with_true(self):
    #     grid = [[True]]
    #     foo = live_neighbor_count(grid)
    #     self.assertEqual(1, foo)
    #
    # def test__stuff_with_false(self):
    #     grid = [[False]]
    #     foo = live_neighbor_count(grid)
    #     self.assertEqual(0, foo)
    #
    # def test__stuff_with_horizontal_true_and_false(self):
    #     grid = [[True], [False]]
    #     foo = live_neighbor_count(grid)
    #     self.assertEqual(1, foo)
    #
    # def test__stuff_with_vertical_true_and_false(self):
    #     grid = [[True, False]]
    #     foo = live_neighbor_count(grid)
    #     self.assertEqual(1, foo)
