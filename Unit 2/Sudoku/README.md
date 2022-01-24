# Sudoku
Sudoku is a logic-based placement game. In classic Sudoku, the objective of the game is to fill a 9x9 grade so that no two numbers repeat in the same row, column, or sub-block. However, Sudoku puzzles can be larger than 9x9, and can have non-equivalent sub-block widths and heights.

## Description
This purpose of this lab is to solve Sudoku problems (not necessarily those from a 9x9 sized board) from a text file.

## Part 1: Backtracking
Backtracking is the recursive process of taking a state, choosing an undetermined space, and trying each available value for that space with a recursive call.

## Part 2: Forward Looking
Forward looking keeps track of all the possible values that each space can hold and updates them. Additionally, failure is returned if any of the spaces become empty (as in no possible value can be placed in that space, so backtracking would become necessary).

To run the Sudoku puzzle solver using backtracking and forward looking, run Sudoku.py with one of the following arguments:
- puzzles_1.txt
- puzzles_2.txt

puzzles_1.txt contains boards that are strictly 9x9 in size, and puzzles_2.txt contains boards that are not restricted to 9x9 in size.