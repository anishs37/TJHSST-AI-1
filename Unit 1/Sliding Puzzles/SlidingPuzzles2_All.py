from heapq import heappush, heappop, heapify
from collections import deque
import math
import time
import sys

file_name = sys.argv[1]
with open(file_name) as f:
    line_list = [line.strip() for line in f]

def parity_check(size, puzzle):
    up_puzzle = puzzle.replace(".", "")
    num_ooop = 0
    overallIter = 0
    iterTest = 0

    while(overallIter < ((size ** 2) - 1)):
        char1 = up_puzzle[iterTest]
        for i in range(iterTest, ((size ** 2) - 1)):      
            char2 = up_puzzle[i]

            if(char1 > char2):
                num_ooop = num_ooop + 1
                #print(char2 + "" + char1)

        iterTest = iterTest + 1
        overallIter = overallIter + 1

    if(size % 2 == 0):
        index_pd = puzzle.index(".")
        row_of_pd = index_pd // size

        if(((row_of_pd % 2 == 0) and (num_ooop % 2 == 1)) or ((row_of_pd % 2 == 1) and (num_ooop % 2 == 0))):
            return True

        else:
            return False
    
    else:
        if(num_ooop % 2 == 1):
            return False
        
        else:
            return True

def taxicab_distance(size, puzzle):
    dist = 0
    sorted_goal_puzzle = sorted(puzzle)
    goal_puzzle = "".join(sorted_goal_puzzle)
    goal_puzzle = goal_puzzle + "."

    expectIndex = 0
    for char in goal_puzzle:
        if(char != "."):
            puzzleIndex = puzzle.index(char)
            row_of_char = puzzleIndex // size
            col_of_char = puzzleIndex % size

            iterTest = size
            iterTest2 = 0
            expected_row = 0
            found = False

            expected_row = expectIndex // size
            expected_col = expectIndex % size
            dist = dist + abs(expected_col - col_of_char) + abs(expected_row - row_of_char)
            expectIndex = expectIndex + 1

    return dist

def find_goal(puzzle):
    goal_puzzle_string = ""

    for char in puzzle:
        if(char.isalpha() or char.isdigit()):
            goal_puzzle_string = goal_puzzle_string + char
    
    sorted_goal_puzzle = sorted(goal_puzzle_string)
    goal_puzzle = "".join(sorted_goal_puzzle)
    goal_puzzle = goal_puzzle + "."
  
    return goal_puzzle 

def goal_test(line):
    goal_state = find_goal(line)

    if(line == goal_state):
        return True
    
    else:
        return False

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

def kDFS(start_state, k):
    fringe = []
    fringe.append((start_state, 0, {start_state}))

    while fringe:
        state, depth, ancestors = fringe.pop()

        if(goal_test(state)):
            return state, depth, len(ancestors) - 1
        
        if(depth < k):
            children_list = get_children(state)

            for c in children_list:
                if(c not in ancestors):
                    c_ancestors = ancestors.copy()
                    c_ancestors.add(c)
                    fringe.append((c, depth + 1, c_ancestors))
    
    return None

def IDDFS(start_state):
    max_depth = 0
    result = None

    while(result == None):
        result = kDFS(start_state, max_depth)
        max_depth = max_depth + 1
    
    return result

def aStar(size, start_state):
    closed = set()
    f = taxicab_distance(size, start_state)
    fringe = []
    heappush(fringe, (f, start_state, 0))

    while fringe:
        heuristic, state, depth = heappop(fringe)

        if(goal_test(state)):
            return len(closed), state, depth
        
        if(state not in closed):
            closed.add(state)
            children_list = get_children(state)

            for c in children_list:
                if c not in closed:
                    new_depth = depth + 1
                    new_f = new_depth + taxicab_distance(size, c)                       
                    heappush(fringe, (new_f, c, new_depth))

    return None

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
    fringe3 = deque()
    fringe4 = deque()

    visited1 = {start_node}
    visited2 = {state_goal}

    fringe1.append((start_node, 0))
    fringe2.append((state_goal, 0))
    fringe3.append(start_node)
    fringe4.append(state_goal)

    visited1.add(start_node)
    visited2.add(state_goal)

    while(any(i in list(fringe3) for i in list(fringe4)) == False):
        state1, moves1 = fringe1.popleft()
        state2, moves2 = fringe2.popleft()

        children_list_1 = get_children(state1)
        for c1 in children_list_1:
            if(c1 not in visited1):
                fringe1.append((c1, moves1 + 1))
                fringe3.append(c1)
                visited1.add(c1)

        children_list_2 = get_children(state2)
        for c2 in children_list_2:
            if(c2 not in visited2):
                fringe2.append((c2, moves2 + 1))
                fringe4.append(c2)
                visited2.add(c2)

    return total_moves

iter = 0

for line in line_list:
    line_list_2 = line.split(" ")
    size = int(line_list_2[0])
    puzzle = line_list_2[1]
    algo = line_list_2[2]
    line = str(size) + " " + puzzle
    string_puzzle = puzzle_string(print_puzzle(line))

    if(algo == "B"):
        start = time.perf_counter()
        if((parity_check(size, puzzle)) == False):
            end = time.perf_counter()
            times = str(end - start)
            print("Line " + str(iter) + ": " + string_puzzle + ", no solution determined in " + times + " seconds")
            
        else:
            start2 = time.perf_counter()
            goal_state, moves = BFS(string_puzzle)
            end2 = time.perf_counter()
            times2 = str(end2- start2)

            print("Line " + str(iter) + ": " + string_puzzle + ", BFS - " + str(moves) + " moves found in " + times2 + " seconds")

    elif(algo == "I"):
        start = time.perf_counter()
        if((parity_check(size, puzzle)) == False):
            end = time.perf_counter()
            times = str(end - start)
            print("Line " + str(iter) + ": " + string_puzzle + ", no solution determined in " + times + " seconds")
            
        else:
            start2 = time.perf_counter()
            goal_state, depth, moves = IDDFS(string_puzzle)
            end2 = time.perf_counter()
            times2 = str(end2- start2)

            print("Line " + str(iter) + ": " + string_puzzle + ", ID-DFS - " + str(moves) + " moves found in " + times2 + " seconds")
    
    elif(algo == "A"):
        start = time.perf_counter()
        if((parity_check(size, puzzle)) == False):
            end = time.perf_counter()
            times = str(end - start)
            print("Line " + str(iter) + ": " + string_puzzle + ", no solution determined in " + times + " seconds")
            
        else:
            start2 = time.perf_counter()
            moves, goal_state, depth = aStar(size, string_puzzle)
            end2 = time.perf_counter()
            times2 = str(end2- start2)

            print("Line " + str(iter) + ": " + string_puzzle + ", A* - " + str(depth) + " moves found in " + times2 + " seconds")
    
    elif(algo == "!"):
        start = time.perf_counter()
        if((parity_check(size, puzzle)) == False):
            end = time.perf_counter()
            times = str(end - start)
            print("Line " + str(iter) + ": " + string_puzzle + ", no solution determined in " + times + " seconds")
            
        else:
            start2 = time.perf_counter()
            goal_state, moves = BFS(string_puzzle)
            end2 = time.perf_counter()
            times2 = str(end2- start2)

            start3 = time.perf_counter()
            goal_state_1, depth1, moves1 = IDDFS(string_puzzle)
            end3 = time.perf_counter()
            times3 = str(end3- start3)

            start4 = time.perf_counter()
            moves2, goal_state_2, depth2 = aStar(size, string_puzzle)
            end4 = time.perf_counter()
            times4 = str(end4- start4)

            print("Line " + str(iter) + ": " + string_puzzle + ", BFS - " + str(moves) + " moves found in " + times2 + " seconds")
            print("Line " + str(iter) + ": " + string_puzzle + ", ID-DFS - " + str(moves1) + " moves found in " + times3 + " seconds")
            print("Line " + str(iter) + ": " + string_puzzle + ", A* - " + str(depth2) + " moves found in " + times4 + " seconds")

    iter = iter + 1
    print("")