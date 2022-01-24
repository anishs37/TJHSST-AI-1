import sys
import time

file_name = sys.argv[1]

with open(file_name) as f:
    puzzle_list = [line.strip() for line in f]

def divisor_list(x):
    list_div = [1]
    sq_rt = x ** 0.5
    iter = 2

    while(iter <= sq_rt):
        if(x % iter == 0):
            if(iter != sq_rt):
                other_num = x / iter
                list_div.append(iter)
                list_div.append(other_num)
            
            else:
                list_div.append(iter)

        iter += 1
    
    return list_div

def find_dimensions(size):
    sqrt_size = size ** 0.5
    n_factors = divisor_list(size)
    sub_height, sub_width = max(i for i in n_factors if i <= sqrt_size), min(i for i in n_factors if i >= sqrt_size)
    return int(sub_height), int(sub_width)

def get_symbol_set(size):
    symb_set = set()
    letters_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    iter = 0

    for i in range(1, n + 1):
        if(i < 10):
            symb_set.add(str(i))
        
        else:
            symb_set.add(letters_list[iter])
            iter = iter + 1
    
    return symb_set

def display_puzzle(new_bd_dict):
    str_to_display = ""
    h_iter = 0
    w_iter = 0
    t_iter = 0

    for elem2 in new_bd_dict:
        elem = new_bd_dict[elem2]
        if(w_iter == subblock_width):
            str_to_display = str_to_display + "| "
            w_iter = 0

        if(t_iter == subblock_width * subblock_height):
            str_to_display = str_to_display + "\n"
            h_iter = h_iter + 1
            t_iter = 0

        if(h_iter == subblock_height):
            for i in range((subblock_width * subblock_height) + subblock_height):
                str_to_display = str_to_display + "- "
            
            h_iter = 0
            str_to_display = str_to_display + "\n"
        
        str_to_display = str_to_display + str(elem) + " "

        t_iter = t_iter + 1
        w_iter = w_iter + 1

    return str_to_display + "|"

def get_constraint_list():
    const_list = []
    iter = 0

    for i in range(n):
        row_set = set()

        for j in range(iter, n + iter):
            row_set.add(j)

        const_list.append(row_set)
        iter = iter + n

    for i in range(n):
        col_set = set()
        iter2 = i
        while(iter2 < (n ** 2)):
            col_set.add(iter2)
            iter2 = iter2 + n
        
        const_list.append(col_set)

    for a in range(0, n, subblock_width):
        for b in range(0, n, subblock_height):
            block_set = set()
            for c in range(a, subblock_width + a):
                for d in range(b, subblock_height + b):
                    score = (d * subblock_width * subblock_height) + c
                    block_set.add(score)

            const_list.append(block_set)

    return const_list

def get_neighbors_dict(const_list):
    neighb_dict = {}

    for i in range(n ** 2):
        set_vals = set()
        for sets in const_list:
            if i in sets:
                for j in sets:
                    if(j != i):
                        set_vals.add(j)
        
        neighb_dict[i] = set_vals

    return neighb_dict

def check_symbols(puzz):
    set_all = set()

    for symb in symbol_set:
        set_all.add(str(puzz.count(symb)))
    
    if(len(set_all) == 1):
        return True
    
    return False

def get_sorted_values(bd_dict_3, var):
    if(var != -1):
        for j in neighbors_dict[var]:
            if(len(bd_dict_3[j]) == 1 and j != var):
                bd_dict_3[var] = bd_dict_3[var].replace(bd_dict_3[j], "")
            
        return set(bd_dict_3[var])
    
    return set()

def get_most_constrained_var(board_dict_to_check):
    min = 99999999
    minIndex = -1

    for k in board_dict_to_check:
        if(1 < len(board_dict_to_check[k]) < min):
            minIndex = k
            min = len(board_dict_to_check[k])
            
    return minIndex

def csp_backtracking_with_forward_looking(board_dict_to_check):
    state = print_state_1(board_dict_to_check)

    if(check_symbols(state) and (state.find('.') == -1) and len(state) == (n ** 2)):
        return state
    
    var = get_most_constrained_var(board_dict_to_check)
    vals = get_sorted_values(board_dict_to_check, var)

    for val in vals:
        new_board_dict_to_check = board_dict_to_check.copy()
        new_board_dict_to_check[var] = val
        new_board_dict_to_check_2 = forward_looking(new_board_dict_to_check, {var})

        if(new_board_dict_to_check_2 is not None):
            result = csp_backtracking_with_forward_looking(new_board_dict_to_check_2)
            new_board_dict_to_check_3 = constraint_propogation(new_board_dict_to_check_2)

            if(new_board_dict_to_check_3 is not None):
                result = csp_backtracking_with_forward_looking(new_board_dict_to_check_3)
                
            if(result is not None):
                return result

    return None

def generate_new_board(state):
    new_bd_dict = {}
    alr_solved = set()

    iter = 0

    for elem in state:
        if(elem == '.'):
            str_to_ret = ''

            for elem in symbol_set:
                str_to_ret = str_to_ret + elem

            new_bd_dict[iter] = str_to_ret
        
        else:
            new_bd_dict[iter] = elem
            alr_solved.add(iter)

        iter = iter + 1
    
    return new_bd_dict, alr_solved

def forward_looking(dict_to_check, solved_list):
    all_indices_solved = set()

    for ind in solved_list:
        all_indices_solved.add(ind)

    while(len(solved_list) != 0):
        elem = solved_list.pop()
        neighbors = neighbors_dict[elem]
        to_replace = dict_to_check[elem]

        for neighb in neighbors:
            elem_at_index = dict_to_check[neighb]
            elem_at_index_2 = elem_at_index.replace(to_replace, "")

            if(len(elem_at_index_2) == 0):
                return None

            dict_to_check[neighb] = elem_at_index_2

            if((len(elem_at_index_2) == 1) and (neighb not in solved_list) and (neighb not in all_indices_solved)):
                solved_list.add(neighb)
                all_indices_solved.add(neighb)

    return dict_to_check

def constraint_propogation(dict_to_check):
    list_solved = set()
    all_test = 0

    for se in constraint_list:
        vals_set = set()
        dict_vals = {}

        for symb in symbol_set:
            dict_vals[symb] = (0, -1)
        
        for c in se:
            vals = dict_to_check[c]

            for elem in vals:
                prevVal, nInd = dict_vals[str(elem)]
                t_vals = (prevVal + 1, c)
                dict_vals[str(elem)] = t_vals
                vals_set.add(elem)
        
        if(len(vals_set) != len(symbol_set)):
            return None

        test = 0
        testIndex = -1
        testSymb = ""

        for check in dict_vals:
            val_to_check, ind = dict_vals[check]

            if(val_to_check == 1):
                test = test + 1
                testIndex = ind
                testSymb = check
        
        if(test == 1):
            old_val = dict_to_check[testIndex]
            old_val_2 = old_val.replace(old_val, testSymb)
            dict_to_check[testIndex] = old_val_2
            list_solved.add(testIndex)
            all_test = all_test + 1
    
    if(all_test != 0):
        dict_to_check_2 = forward_looking(dict_to_check, list_solved)

        if(dict_to_check_2 is not None):
            return dict_to_check_2
        
        else:
            return None
    
    return dict_to_check

def print_state():
    str_to_ret = ""

    for key in new_board_dict:
        str_to_ret = str_to_ret + new_board_dict[key]
    
    return str_to_ret

def print_state_1(bd_dict_2):
    str_to_ret = ""

    for key in bd_dict_2:
        str_to_ret = str_to_ret + bd_dict_2[key]
    
    return str_to_ret

start = time.perf_counter()

for puzzle in puzzle_list:
    n = int(len(puzzle) ** 0.5)
    subblock_height, subblock_width = find_dimensions(n)
    symbol_set = get_symbol_set(n)
    constraint_list = get_constraint_list()
    neighbors_dict = get_neighbors_dict(constraint_list)
    new_board_dict, already_solved = generate_new_board(puzzle)

    new_bd_dict_2 = forward_looking(new_board_dict, already_solved)
    print(csp_backtracking_with_forward_looking(new_bd_dict_2))

end = time.perf_counter()
print(str(end - start) + " seconds total")