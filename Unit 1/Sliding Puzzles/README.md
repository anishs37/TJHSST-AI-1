# Sliding Puzzles
Programs that return the minimum number of moves it will take to solve a sliding puzzle.

## Description
Sliding puzzles are combination puzzles where a player has to slide the tiles (in this case, numbers for a 3x3 board, and letters for a larger board). Reading left-to-right starting from the top left of the board, all the numbers or letters should go in order based on the ASCII table, with one space (represented by a period) on the bottom-right of the board. The programs I have coded will solve sliding puzzles using a variety of algorithms.

## Part 1: BFS and BiBFS
Solving a file of sliding puzzles using either BFS or BiBFS.

BFS: Run SlidingPuzzles1_BFS.py with 15_puzzles.txt as an argument.
Bi-BFS: Run SlidingPuzzles1_BiBFS.py with 15_puzzles.txt as an argument.

## Part 2: Adding ID-DFS and A*
Solving a file of sliding puzzles using either BFS, ID-DFS, A*, or all algorithms based on the argument.

To run Part 2, run SlidingPuzzles2_All.py, with slide_puzzle_tests.txt as an argument.