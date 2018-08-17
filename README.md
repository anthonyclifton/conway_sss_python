Conway's Game of Life Skeleton
==============================

This is a skeleton for an implementation of Conway's Game of Life
in Python.  It uses ncurses to display output in the terminal.

The grid is technically infinite up to Python's and the platform's
MAXINT.  However, the skeleton currently displays coordinates (0, 0)
in the upper left corner with X increasing to the right and Y increasing
down.

This implementation can load an initial cell pattern from a csv file
specified in a configuration file.

The skeleton implementation in the master branch of this repository
only knows how to place random cells on the grid for a moment and then
replace them with subsequent random cells.

The intention is that you can use this is a framework to build your own
implementation of the game, test driving the rules.  The framework provides
configuration loading and a screen service for output.  Mostly all you
have to worry about is the game logic.  Though you should feel free to
modify the framework to suit your hopes, dreams, wants, and desperate
needs.

Configuration and Run Instructions
==================================

No build is necessary to run this software.  You can simply execute:

```python conway.py```

from the root of the project tree.

Your terminal can be set to any dimension and the screen service will
expand to use it, and display more of the grid.

To quit the program, you can use the ```q``` or ```Q``` key.

Your Goal
=========

Using this skeleton, test drive a working implementation of Conway's
Game of Life.  Technically, you don't *have* to use the skeleton.  You
can start from scratch.  But the skeleton gives you some basic display
technology, an update/display loop, hooks for adding keyboard control
of your implementation, and lots of test examples.

The test examples come in various flavors.  ```test_file_service.py```
is an integration test that reads a real file on the file system and
outputs some transformed data.   ```test_grid.py``` is basic unit
testing that doesn't require test doubles.  ```test_screen_service.py```
is a very "Mockist" approach to unit testing while ```test_game.py```
makes use of a test double called a "Fake."

Three initial grids are provided in the ```patterns``` directory of the project.
In Conway terminology, the patterns are sometimes called "seeds."  These
represent an interesting initial state for the program.

You can verify that your program is working correctly by programming it to
load one of these with ```read_cells()``` method in ```file_service.py```

'oscillator.csv' is a simple three cell oscillator.

`test.csv` is a very simple cell pattern that grows in fun ways.

`gosper-glider-gun.csv` is Bill Gosper's Glider Gun which produces gliders forever.

Example Implementations
=======================

This repository also includes two branches with working implementations.  They will
show other styles of testing, more sophisticated approaches to software design,
and hints about achieving good performance as the number of live cells increases
on your grid.

Anthony C - https://github.com/anthonyclifton/conway_sss_python/tree/implement-conway

Michael P - https://github.com/anthonyclifton/conway_sss_python/tree/michael

Rules
=====

_Any live cell with fewer than two live neighbours dies, as if caused by underpopulation._

_Any live cell with two or three live neighbours lives on to the next generation._

_Any live cell with more than three live neighbours dies, as if by overpopulation._

_Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction._
