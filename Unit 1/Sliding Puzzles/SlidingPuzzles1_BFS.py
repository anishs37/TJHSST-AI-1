from collections import deque
import math
import time
import sys

file_name = sys.argv[1]
with open(file_name) as f:
    line_list = [line.strip() for line in f]

def puzzle_string_1(line):
    elem_line = line.split(" ")
    puzzle = elem_line[1]
    return puzzle

def puzzle_string(puzzle):
    string_to_ret = ''
    total_board_size = int(len(puzzle))

    iter = 0

    while(iter < total_board_size):
        string_to_ret = string_to_ret + puzzle[iter]
        iter = iter + 2
    
    return string_to_ret

def print_puzzle(line):
    elem_line = line.split(" ")
    board_size, puzzle = int(elem_line[0]), elem_line[1]
    iter = 0
    print_puzzle = ""
    while(iter < board_size * board_size):
        for i in range(board_size):
            if(i != board_size - 1):
                print_puzzle = print_puzzle + puzzle[iter + i] + " "
            
            else:
                print_puzzle = print_puzzle + puzzle[iter + i]
        
        iter += board_size

        if(iter != board_size ** 2):
            print_puzzle = print_puzzle + "\n"

    return print_puzzle

def find_goal(puzzle):
    goal_puzzle_string = ""

    for char in puzzle:
        if(char.isalpha() or char.isdigit()):
            goal_puzzle_string = goal_puzzle_string + char
    
    sorted_goal_puzzle = sorted(goal_puzzle_string)
    goal_puzzle = "".join(sorted_goal_puzzle)
    goal_puzzle = goal_puzzle + "."
  
    return goal_puzzle 

def get_children(line):
    children_list = []
    puzzle = line
    total_size = len(puzzle)
    board_size = int(total_size ** 0.5)

    matrix = [[0]*board_size for i in range(board_size)]

    iter = 0

    for i in range(board_size):
        for j in range(board_size):
            matrix[i][j] = puzzle[iter]
            iter = iter + 1
    
    x, y = 0, 0

    for i in range(board_size):
        for j in range(board_size):
            if(matrix[i][j] == '.'):
                x, y = i, j
    
    if(x != 0):
        string_to_add = ''
        val = matrix[x - 1][y]
        matrix[x - 1][y] = '.'
        matrix[x][y] = val

        for i in range(board_size):
            for j in range(board_size):
                string_to_add = string_to_add + matrix[i][j]
        
        matrix[x][y] = '.'
        matrix[x - 1][y] = val

        children_list.append(string_to_add)
    
    if(x != board_size - 1):
        string_to_add = ''
        val = matrix[x + 1][y]
        matrix[x + 1][y] = '.'
        matrix[x][y] = val

        for i in range(board_size):
            for j in range(board_size):
                string_to_add = string_to_add + matrix[i][j]
        
        matrix[x][y] = '.'
        matrix[x + 1][y] = val

        children_list.append(string_to_add)

    if(y != 0):
        string_to_add = ''
        val = matrix[x][y - 1]
        matrix[x][y - 1] = '.'
        matrix[x][y] = val

        for i in range(board_size):
            for j in range(board_size):
                string_to_add = string_to_add + matrix[i][j]
        
        matrix[x][y] = '.'
        matrix[x][y - 1] = val

        children_list.append(string_to_add)
    
    if(y != board_size - 1):
        string_to_add = ''
        val = matrix[x][y + 1]
        matrix[x][y + 1] = '.'
        matrix[x][y] = val

        for i in range(board_size):
            for j in range(board_size):
                string_to_add = string_to_add + matrix[i][j]
        
        matrix[x][y] = '.'
        matrix[x][y + 1] = val

        children_list.append(string_to_add)

    return children_list
    

def goal_test(line):
    goal_state = find_goal(line)

    if(line == goal_state):
        return True
    
    else:
        return False

def BFS(start_node):
    fringe = deque()
    visited = {start_node}
    fringe.append((start_node, 0))
    visited.add(start_node)
    
    while fringe:
        state, moves = fringe.popleft()

        if(goal_test(state)):
            return state, moves
        
        else:
            children_list = get_children(state)
            for c in children_list:
                if(c not in visited):
                    fringe.append((c, moves + 1))
                    visited.add(c)
    
    return None, 999999

iter = 0

for line in line_list:
    line = "4 " + line
    start = time.perf_counter()
    string_puzzle = puzzle_string(print_puzzle(line))
    goal_state, moves = BFS(string_puzzle)
    end = time.perf_counter()
    times = str(end - start)
    print("Line " + str(iter) + ": " + string_puzzle + ", " + str(moves) + " moves found in " + times + " seconds")
    iter = iter + 1