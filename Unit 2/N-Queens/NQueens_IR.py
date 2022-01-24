import sys
import time
import random
from random import randint

def display_puzzle(size, mat):
    string_to_print = ""
    
    for i in range(size):
        for j in range(size):
            val = mat[i][j]
            string_to_print = string_to_print + val + " "

        string_to_print = string_to_print + "\n"

    print(string_to_print)

def generate_random_state(size):
    val = size // 2
    matrix = [["0"]*size for i in range(size)]
    iter = 0
    iter2 = 0

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

    for i in range(size):
        num_conf = 0
        for j in range(size):
            if(mat[i][j] == '*'):
                num_conf = num_conf + check_at_loc(i, j, size, mat)
                list_indices[i] = num_conf

    return list_indices

def list_vals():
    list_to_ret = []

    for i in range(board_size_2):
        for j in range(board_size_2):
            if(mat[i][j] == '*'):
                list_to_ret.append(j)
    
    return list_to_ret

def place_queen_at_min(size, max_row):
    list_conf = [0 for i in range(size)]
    val = 0

    for j in range(size):
        num_conf = check_at_loc(max_row, j, size, mat)
        list_conf[j] = num_conf

        if(mat[max_row][j] == '*'):
            val = j
    
    return list_conf, val

start_7 = time.perf_counter()

#will run on boards of sizes 33 and 36
for i in range(33, 37, 3):
    board_size_2 = i
    mat = generate_random_state(board_size_2)
    print(list_vals())
    print("Iniitial number of conflicts: " + str(num_conflicts(board_size_2, mat)))
    print("")

    iter_7 = 0

    while(num_conflicts(board_size_2, mat) != 0):
        conf_list = num_conflicts_list(board_size_2, mat)

        max_val_list = []
        max_stuff = max(conf_list)

        for index, elem in enumerate(conf_list):
            if(elem == max_stuff):
                max_val_list.append((index))

        max_index = random.choice(max_val_list)

        list_check, val = place_queen_at_min(board_size_2, max_index)
        min_conf = min(list_check)
        min_conf_list = []

        for index2, elem2 in reversed(list(enumerate(list_check))):
            if(elem2 == min_conf):
                min_conf_list.append(index2)

        min_conf_index = random.choice(min_conf_list)

        if(min_conf_index != val):
            mat[max_index][min_conf_index] = '*'
            mat[max_index][val] = '0'

        print(list_vals())
        print("Number of conflicts: " + str(num_conflicts(board_size_2, mat)))
        iter_7 = iter_7 + 1


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

    print(test_solution(list_vals()))
    print("")
    print("")

end_7 = time.perf_counter()
print("Total time: " + str(end_7 - start_7) + " seconds")