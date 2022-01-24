import sys
import time
import random
from random import randint

def generate_random_state(size):
    matrix = [["0"]*size for i in range(size)]
    iter = 0

    for i in range(size):
        matrix[i][iter] = '*'

        if((size - iter) <= 2):
            iter = 1
            
        else:
            iter = iter + 2
    
    return matrix

def check_at_loc(x, y, board_size, mat):
    all_locs = set()
    test = 0
    for upc in range(board_size):
        if(mat[upc][y] == "*" and (upc, y) != (x, y)):
            all_locs.add((upc, y))
    
    for i, k in zip(range(x, -1, -1), range(y, -1, -1)):
        if(mat[i][k] == '*' and (i, k) != (x, y)):
            all_locs.add((i, k))

    for i, k in zip(range(x, board_size, 1), range(y, -1, -1)):
        if(mat[i][k] == '*' and (i, k) != (x, y)):
            all_locs.add((i, k))

    for i, k in zip(range(x, -1, -1), range(y, board_size, 1)):
        if(mat[i][k] == '*' and (i, k) != (x, y)):
            all_locs.add((i, k))

    for i, k in zip(range(x, board_size, 1), range(y, board_size, 1)):
        if(mat[i][k] == '*' and (i, k) != (x, y)):
            all_locs.add((i, k))

    return len(all_locs)
    
def num_conflicts(size, mat):
    num_conf = 0
    for i in range(size):
        for j in range(size):
            if(mat[i][j] == '*'):
                num_conf = num_conf + check_at_loc(i, j, size, mat)

    return num_conf

def num_conflicts_list(size, mat):
    list_indices = [0 for i in range(size)]
    vals_list = list_vals()

    for i in range(size):
        num_conf = 0
        for j in range(size):
            if(mat[i][j] == '*'):
                num_conf = num_conf + check_at_loc(i, j, size, mat)
        list_indices[i] = num_conf

    return list_indices

def list_vals(mat):
    list_to_ret = []

    i_iter = 0
    j_iter = 0

    while(i_iter < board_size):
        if(mat[i_iter][j_iter] != "*"):
            j_iter = j_iter + 1
        
        else:
            list_to_ret.append(j_iter)
            i_iter = i_iter + 1
            j_iter = 0

    return list_to_ret

def place_queen_at_min(size, max_row, mat):
    list_conf = [0 for i in range(size)] 
    val = 0

    for j in range(size):
        num_conf = check_at_loc(max_row, j, size, mat)
        list_conf[j] = num_conf

        if(mat[max_row][j] == '*'):
            #print(val)
            val = j
    
    return list_conf, val

def display_puzzle(l_vals):
    mat  = [["0"]*board_size for i in range(board_size)]
    
    for i in range(board_size):
        mat[i][l_vals[i]] = '*'

    string_to_print = ""
    
    for i in range(board_size):
        for j in range(board_size):
            val = mat[i][j]
            string_to_print = string_to_print + val + " "

        string_to_print = string_to_print + "\n"

    print(string_to_print)

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

list_to_check = []

start = time.perf_counter()
allSolved = False

iter = 8

while((time.perf_counter() - start) < 30):
    board_size = iter
    if((iter % 6 != 2) and (iter % 6 != 3)):
        list_evens = [j for j in range(0, iter, 2)]
        list_odds = [k for k in range(1, iter, 2)]
        total_list = list_odds + list_evens
        list_to_check.append(total_list)
    
    else:
        list_evens = [j for j in range(0, iter, 2)]
        list_odds = [k for k in range(1, iter, 2)]      

        if(iter % 6 == 2):
            list_evens[0] = 2
            list_evens[1] = 0
            list_evens.remove(4)
            list_evens.append(4)

        else:
            list_odds.remove(1)
            list_odds.append(1)
            list_evens.remove(0)
            list_evens.remove(2)
            list_evens.append(0)
            list_evens.append(2)

        total_list = list_odds + list_evens

        check_bool = test_solution(total_list)

        if(check_bool == False):
            print("FALSE HERE: " + str(iter))
        
        else:
            print("TRUE HERE: " + str(iter))

        list_to_check.append(total_list)
    
    iter = iter + 1

end = time.perf_counter()
total_time = end - start

print(str(len(list_to_check) + 7) + " max size in 30 seconds")
print(str(total_time) + " seconds taken total")