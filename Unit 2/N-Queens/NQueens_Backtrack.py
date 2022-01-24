import sys
import time
import random

def test_solution(state):
    for var in range(len(state)):
        left = state[var]
        middle = state[var]
        right = state[var]
        for compare in range(var + 1, len(state)):
            left -= 1
            right += 1
            if state[compare] == middle:
                print(var, "middle", compare)
                return False
            if left >= 0 and state[compare] == left:
                print(var, "left", compare)
                return False
            if right < len(state) and state[compare] == right:
                print(var, "right", compare)
                return False
    
    return True

def define_state(start_size):
    strToRet = ""

    for i in range(start_size ** 2):
        strToRet = strToRet + '.'
    
    return strToRet
    
def goal_test(state):
    total_size = len(state)
    board_size = int(total_size ** 0.5)

    matrix = [[0]*board_size for i in range(board_size)]

    if(state.count('*') == board_size):
        return True

    return False

def get_next_unassigned_var(state):
    total_size = len(state)
    board_size = int(total_size ** 0.5)

    matrix = [[0]*board_size for i in range(board_size)]

    iter = 0

    for i in range(board_size):
        for j in range(board_size):
            matrix[i][j] = state[iter]
            iter = iter + 1

    for i in range(board_size):
        testIter = 0
        for j in range(board_size):
            if(matrix[i][j] == '*'):
                testIter = testIter + 1
        
        if(testIter == 0):
            return i

def get_sorted_values(state, var):
    list_sorted = []
    total_size = len(state)
    board_size = int(total_size ** 0.5)

    matrix = [[0]*board_size for i in range(board_size)]

    iter = 0

    for i in range(board_size):
        for j in range(board_size):
            matrix[i][j] = state[iter]
            iter = iter + 1

    nums = list(range(0, board_size))
    random.shuffle(nums)

    for j in nums:
        test = 0
        for upc in range(board_size):
            if(matrix[upc][j] == "*"):
                test = test + 1
        
        if(test == 0):
            lst1 = range(var, -1, -1)
            lst2 = range(j, -1, -1)
            for i, k in zip(lst1, lst2):
                if(matrix[i][k] == '*'):
                    test = test + 1

        if(test == 0):
            lst1 = range(var, -1, -1)
            lst2 = range(j, board_size, 1)
            for i, k in zip(lst1, lst2):
                if(matrix[i][k] == '*'):
                    test = test + 1

        if(test == 0):
            list_sorted.append(j)

    return list_sorted

def print_puzzle(line):
    total_size = len(line)
    board_size = int(total_size ** 0.5)
    puzzle = line
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

def get_vals(state):
    list_sorted_1 = []
    total_size = len(state)
    board_size = int(total_size ** 0.5)

    matrix = [[0]*board_size for i in range(board_size)]

    iter = 0

    for i in range(board_size):
        for j in range(board_size):
            matrix[i][j] = state[iter]
            iter = iter + 1
    
    for i in range(board_size):
        for j in range(board_size):
            if(matrix[i][j] == '*'):
                list_sorted_1.append(j)
    
    return list_sorted_1


def csp_backtracking(state):
    total_size = len(state)
    board_size = int(total_size ** 0.5)

    if(goal_test(state)):
        return state
    
    var = get_next_unassigned_var(state)
    vals = get_sorted_values(state, var)
    for val in vals:
        in_btw_val = (board_size * var) + val
        new_state = state[0:in_btw_val] + "*" + state[in_btw_val + 1:]
        result = csp_backtracking(new_state)
        
        if result is not None:
            return result

    return None

start = time.perf_counter()

#size of 31
state1 = define_state(31)
solved_state = csp_backtracking(state1)
test1 = get_vals(solved_state)
print(test1)
print(test_solution(test1))
print("")

#size of 33
state = define_state(33)
solved_state = csp_backtracking(state)
test2 = get_vals(solved_state)
print(test2)
print(test_solution(test2))
print("")

end = time.perf_counter()
print("time taken: " + str(end - start))