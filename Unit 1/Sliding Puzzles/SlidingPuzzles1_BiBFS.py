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

def BiBFS(start_node):
    len_nodes = len(start_node)
    state_goal = ''.join(sorted(start_node))
    state_goal = state_goal[1:] + "."
    total_moves = 0

    fringe1 = deque()
    fringe2 = deque()
    fringe3 = {start_node : 0}
    fringe4 = {state_goal : 0}
    fringe5 = deque()
    fringe6 = deque()

    visited1 = {start_node}
    visited2 = {state_goal}

    fringe1.append((start_node, 0))
    fringe2.append((state_goal, 0))
    fringe3 = {start_node : 0}
    fringe4 = {state_goal : 0}
    fringe5.append(start_node)
    fringe6.append(start_node)

    visited1.add(start_node)
    visited2.add(state_goal)

    iter = 0

    visitedFalse = 0
    fringeFalse = 0

    while(bool(visited1 & visited2) == False):
        if(bool(set(fringe1) & set(fringe2))):
            fringeFalse = 1
        
        else:
            #print("in here")
            state1, moves1 = fringe1.popleft()
            state2, moves2 = fringe2.popleft()

            children_list_1 = get_children(state1)
            for c1 in children_list_1:
                if(c1 not in visited1):
                    fringe1.append((c1, moves1 + 1))
                    fringe3[c1] = moves1 + 1
                    fringe5.append(c1)
                    visited1.add(c1)

            children_list_2 = get_children(state2)
            for c2 in children_list_2:
                if(c2 not in visited2):
                    fringe2.append((c2, moves2 + 1))
                    fringe4[c2] = moves2 + 1
                    fringe6.append(c2)
                    visited2.add(c2)

            iter = iter + 1

    if(fringeFalse == 1):
        intersection_list = list(set(list(fringe5)).intersection(set(list(fringe6))))
        num1 = fringe3.get(intersection_list[0])
        num2 = fringe4.get(intersection_list[0])
        total_moves = num1 + num2
        return total_moves
    
    else:
        intersection_list = list(set(list(visited1)).intersection(set(list(visited2))))
        num1 = fringe3.get(intersection_list[0])
        num2 = fringe4.get(intersection_list[0])
        total_moves = num1 + num2
        return total_moves


iter = 0

for line in line_list:
    line = "4 " + line
    string_puzzle = puzzle_string(print_puzzle(line))

    start1 = time.perf_counter()
    moves_1 = BiBFS(string_puzzle)
    end1 = time.perf_counter()
    times_1 = str(end1 - start1)
    print("Line " + str(iter) + ": " + string_puzzle + ", " + str(moves_1) + " moves found in " + times_1 + " seconds")
    iter = iter + 1