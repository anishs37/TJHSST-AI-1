# Ghost
Ghost is a word game where the objective of the game is for a turn to not end on you. Specifically:

- Players take turns each writing a letter.
- Every time a letter is written, the sequence of letters so far must be the beginning of at least one valid word.
- If the turn ends on you (which is a valid word satisfying the minimum length argument is made), you lose.
- Short words don’t count (and is specified as an argument).

## Description
This purpose of this lab is to represent the possible moves where the next player can guarantee victory.

## Part 1: Two-Player Ghost using Negamax with A/B Pruning
A two-player ghost game is modeled, and the AI will determine the possible moves where the next player can guarantee victory.

To run the two-player version of Ghost, run ghost_two.py with the following arguments:
- Argument #1: The name of a dictionary (either wordlist.txt or words_all.txt)
- Argument #2: The minimum length of the word
- Argument #3: (Optional) A game in progress (if no argument is provided, it will be assumed that a new game is starting)

## Part 2: Three-Player Ghost using Maximax
A three-player ghost game is modeled, and the AI will determine the possible moves where the next player can guarantee victory.

To run the three-player version of Ghost, run ghost_three.py with the following arguments:
- Argument #1: The name of a dictionary (either wordlist.txt or words_all.txt)
- Argument #2: The minimum length of the word
- Argument #3: (Optional) A game in progress (if no argument is provided, it will be assumed that a new game is starting)

This lab was completed with a partner.