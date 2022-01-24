import random
import time

def possible_moves(board, token):
    list_possible = set()
    opposite_token = 'x'

    if(token == 'x'):
        opposite_token = 'o'

    matrix = [[0 for l in range(8)] for k in range(8)]

    iter = 0

    for elem in board:
        matrix[int(iter / 8)][int(iter % 8)] = elem
        iter = iter + 1
    
    for i in range(8):
        for j in range(8):
            elem = matrix[i][j]

            if(elem == token):
                test_cons = 0
                test_i = i
                test_j = j

                # move up
                
                while(test_i > 0):
                    test_i = test_i - 1
                    elem2 = matrix[test_i][test_j]

                    if(elem2 == token or (elem2 == '.' and test_cons == 0)):
                        break
                
                    else:
                        test_cons = test_cons + 1

                        if(elem2 == '.'):
                            elem_ind = (test_i * 8) + test_j
                            list_possible.add(elem_ind)
                            break
                
                test_cons = 0
                test_i = i
                test_j = j

                # move down

                while(test_i < 7):
                    test_i = test_i + 1
                    elem2 = matrix[test_i][test_j]

                    if(elem2 == token or (elem2 == '.' and test_cons == 0)):
                        break
                
                    else:
                        test_cons = test_cons + 1

                        if(elem2 == '.'):
                            elem_ind = (test_i * 8) + test_j
                            list_possible.add(elem_ind)
                            break

                test_cons = 0
                test_i = i
                test_j = j

                # move right

                while(test_j < 7):
                    test_j = test_j + 1
                    elem2 = matrix[test_i][test_j]

                    if(elem2 == token or (elem2 == '.' and test_cons == 0)):
                        break
                
                    else:
                        test_cons = test_cons + 1

                        if(elem2 == '.'):
                            elem_ind = (test_i * 8) + test_j
                            list_possible.add(elem_ind)
                            break
                
                test_cons = 0
                test_i = i
                test_j = j

                # move left

                while(test_j > 0):
                    test_j = test_j - 1
                    elem2 = matrix[test_i][test_j]

                    if(elem2 == token or (elem2 == '.' and test_cons == 0)):
                        break
                
                    else:
                        test_cons = test_cons + 1

                        if(elem2 == '.'):
                            elem_ind = (test_i * 8) + test_j
                            list_possible.add(elem_ind)
                            break
                
                test_cons = 0
                test_i = i
                test_j = j

                # move up-left

                while(test_i > 0 and test_j > 0):
                    test_i = test_i - 1
                    test_j = test_j - 1
                    elem2 = matrix[test_i][test_j]

                    if(elem2 == token or (elem2 == '.' and test_cons == 0)):
                        break
                
                    else:
                        test_cons = test_cons + 1

                        if(elem2 == '.'):
                            elem_ind = (test_i * 8) + test_j
                            list_possible.add(elem_ind)
                            break
                
                test_cons = 0
                test_i = i
                test_j = j

                # move up-right

                while(test_i > 0 and test_j < 7):
                    test_i = test_i - 1
                    test_j = test_j + 1
                    elem2 = matrix[test_i][test_j]

                    if(elem2 == token or (elem2 == '.' and test_cons == 0)):
                        break
                
                    else:
                        test_cons = test_cons + 1

                        if(elem2 == '.'):
                            elem_ind = (test_i * 8) + test_j
                            list_possible.add(elem_ind)
                            break
                
                test_cons = 0
                test_i = i
                test_j = j

                # move down-left

                while(test_i < 7 and test_j > 0):
                    test_i = test_i + 1
                    test_j = test_j - 1
                    elem2 = matrix[test_i][test_j]

                    if(elem2 == token or (elem2 == '.' and test_cons == 0)):
                        break
                
                    else:
                        test_cons = test_cons + 1

                        if(elem2 == '.'):
                            elem_ind = (test_i * 8) + test_j
                            list_possible.add(elem_ind)
                            break
                
                test_cons = 0
                test_i = i
                test_j = j

                # move down-right

                while(test_i < 7 and test_j < 7):
                    test_i = test_i + 1
                    test_j = test_j + 1
                    elem2 = matrix[test_i][test_j]

                    if(elem2 == token or (elem2 == '.' and test_cons == 0)):
                        break
                
                    else:
                        test_cons = test_cons + 1

                        if(elem2 == '.'):
                            elem_ind = (test_i * 8) + test_j
                            list_possible.add(elem_ind)
                            break
                
                test_cons = 0
                test_i = i
                test_j = j

    list_possible_1 = list(list_possible)                   

    return list_possible_1

def make_move(board, token, index):
    board = board[:index] + token + board[index + 1:]

    matrix = [[0 for l in range(8)] for k in range(8)]

    iter = 0

    for elem in board:
        matrix[int(iter / 8)][int(iter % 8)] = elem
        iter = iter + 1

    i = int(index / 8)
    j = int(index % 8)

    test_i = i
    test_j = j
    test_cons = 0

    #up

    while(test_i > 0):
        test_i = test_i - 1
        elem = matrix[test_i][test_j]

        if(elem == '.' or (elem == token and test_cons == 0)):
            break

        else:
            test_cons = test_cons + 1

            if(elem == token):
                test_i_2 = test_i + 1
                elem_2 = matrix[test_i_2][test_j]

                while(elem_2 != token):
                    matrix[test_i_2][test_j] = token
                    test_i_2 = test_i_2 + 1
                    elem_2 = matrix[test_i_2][test_j]
                
                break
    
    test_i = i
    test_j = j
    test_cons = 0

    #down

    while(test_i < 7):
        test_i = test_i + 1
        elem = matrix[test_i][test_j]

        if(elem == '.' or (elem == token and test_cons == 0)):
            break

        else:
            test_cons = test_cons + 1

            if(elem == token):
                test_i_2 = test_i - 1
                elem_2 = matrix[test_i_2][test_j]

                while(elem_2 != token):
                    matrix[test_i_2][test_j] = token
                    test_i_2 = test_i_2 - 1
                    elem_2 = matrix[test_i_2][test_j]
                
                break
    
    test_i = i
    test_j = j
    test_cons = 0

    #left

    while(test_j > 0):
        test_j = test_j - 1
        elem = matrix[test_i][test_j]

        if(elem == '.' or (elem == token and test_cons == 0)):
            break

        else:
            test_cons = test_cons + 1

            if(elem == token):
                test_j_2 = test_j + 1
                elem_2 = matrix[test_i][test_j_2]

                while(elem_2 != token):
                    matrix[test_i][test_j_2] = token
                    test_j_2 = test_j_2 + 1
                    elem_2 = matrix[test_i][test_j_2]
                
                break
    
    test_i = i
    test_j = j
    test_cons = 0

    #right

    while(test_j < 7):
        test_j = test_j + 1
        elem = matrix[test_i][test_j]

        if(elem == '.' or (elem == token and test_cons == 0)):
            break

        else:
            test_cons = test_cons + 1

            if(elem == token):
                test_j_2 = test_j - 1
                elem_2 = matrix[test_i][test_j_2]

                while(elem_2 != token):
                    matrix[test_i][test_j_2] = token
                    test_j_2 = test_j_2 - 1
                    elem_2 = matrix[test_i][test_j_2]
                
                break
    
    test_i = i
    test_j = j
    test_cons = 0

    #up-left

    while(test_i > 0 and test_j > 0):
        test_i = test_i - 1
        test_j = test_j - 1
        elem = matrix[test_i][test_j]

        if(elem == '.' or (elem == token and test_cons == 0)):
            break

        else:
            test_cons = test_cons + 1

            if(elem == token):
                test_i_2 = test_i + 1
                test_j_2 = test_j + 1
                elem_2 = matrix[test_i_2][test_j_2]

                while(elem_2 != token):
                    matrix[test_i_2][test_j_2] = token
                    test_i_2 = test_i_2 + 1
                    test_j_2 = test_j_2 + 1
                    elem_2 = matrix[test_i_2][test_j_2]
                
                break

    test_i = i
    test_j = j
    test_cons = 0

    #down-right

    while(test_i < 7 and test_j < 7):
        test_i = test_i + 1
        test_j = test_j + 1
        elem = matrix[test_i][test_j]

        if(elem == '.' or (elem == token and test_cons == 0)):
            break

        else:
            test_cons = test_cons + 1

            if(elem == token):
                test_i_2 = test_i - 1
                test_j_2 = test_j - 1
                elem_2 = matrix[test_i_2][test_j_2]

                while(elem_2 != token):
                    matrix[test_i_2][test_j_2] = token
                    test_i_2 = test_i_2 - 1
                    test_j_2 = test_j_2 - 1
                    elem_2 = matrix[test_i_2][test_j_2]
                
                break
    
    test_i = i
    test_j = j
    test_cons = 0

    #up-right

    while(test_i > 0 and test_j < 7):
        test_i = test_i - 1
        test_j = test_j + 1
        elem = matrix[test_i][test_j]

        if(elem == '.' or (elem == token and test_cons == 0)):
            break

        else:
            test_cons = test_cons + 1

            if(elem == token):
                test_i_2 = test_i + 1
                test_j_2 = test_j - 1
                elem_2 = matrix[test_i_2][test_j_2]

                while(elem_2 != token):
                    matrix[test_i_2][test_j_2] = token
                    test_i_2 = test_i_2 + 1
                    test_j_2 = test_j_2 - 1
                    elem_2 = matrix[test_i_2][test_j_2]
                
                break
                

    test_i = i
    test_j = j
    test_cons = 0

    #down-left

    while(test_i < 7 and test_j > 0):
        test_i = test_i + 1
        test_j = test_j - 1
        elem = matrix[test_i][test_j]

        if(elem == '.' or (elem == token and test_cons == 0)):
            break

        else:
            test_cons = test_cons + 1

            if(elem == token):
                test_i_2 = test_i - 1
                test_j_2 = test_j + 1
                elem_2 = matrix[test_i_2][test_j_2]

                while(elem_2 != token):
                    matrix[test_i_2][test_j_2] = token
                    test_i_2 = test_i_2 - 1
                    test_j_2 = test_j_2 + 1
                    elem_2 = matrix[test_i_2][test_j_2]
                
                break

    board_2 = ''

    for k in range(8):
        for l in range(8):
            board_2 = board_2 + matrix[k][l]

    return board_2

def score(board):
    if(board.count('.') == 0):
        x_count = board.count('x')
        o_count = board.count('o')

        score = ((x_count - o_count) * 100000000000000000000000000000)
        return score

    score = 0
    corner_index_list = [0, 0, 0, 7, 7, 7, 56, 56, 56, 63, 63, 63]
    next_to_corner_index_list = [1, 8, 9, 6, 14, 15, 48, 49, 57, 54, 55, 62]
    edge_list = [2, 3, 4, 5, 16, 24, 32, 40, 58, 59, 60, 61, 23, 31, 39, 47]
    two_away_list = [16, 23, 40, 47]

    for num in two_away_list:
        if(board[num] == 'x'):
            score = score + 40000
        
        if(board[num] == 'o'):
            score = score - 40000

    for corn in corner_index_list:
        if(board[corn] == 'o'):
            score = score - 500000

        if(board[corn] == 'x'):
            score = score + 500000

    for edge in edge_list:
        if(board[edge] == 'o'):
            score = score - 60000
        
        if(board[edge] == 'x'):
            score = score + 60000

    for next_corn, corn_check in zip(next_to_corner_index_list, corner_index_list):
        if(board[next_corn] == 'x' and board[corn_check] == '.'):
            score = score - 250000

        if(board[next_corn] == 'x' and board[corn_check] == 'x'):
            score = score + 250000

        if(board[next_corn] == 'o' and board[corn_check] == '.'):
            score = score + 250000

        if(board[next_corn] == 'o' and board[corn_check] == 'o'):
            score = score - 250000

    for i in range(0, 56, 7):
        string_check = board[i:i + 8]

        if(string_check.count('x') >= 7):
            score = score + 100000
        
        if(string_check.count('o') >= 7):
            score = score - 100000
    
    for i in range(0, 8):
        string_check = board[i:64:8]

        if(string_check.count('x') >= 7):
            score = score + 100000
        
        if(string_check.count('o') >= 7):
            score = score - 100000

    diag_1 = board[0:64:9]
    diag_2 = board[7:57:7]

    if(diag_1.count('x') >= 7):
        score = score + 100000
    
    if(diag_1.count('o') >= 7):
        score = score - 100000
    
    if(diag_2.count('x') >= 7):
        score = score + 100000

    if(diag_2.count('o') >= 7):
        score = score - 100000

    poss_to_move = len(possible_moves(board, 'x'))
    poss_to_move_2 = len(possible_moves(board, 'o'))

    score = score + (poss_to_move - poss_to_move_2) * 300000
    return score

def game_over(board):
    poss_to_move = len(possible_moves(board, 'x'))
    poss_to_move_2 = len(possible_moves(board, 'o'))

    if(poss_to_move + poss_to_move_2 == 0):
        return True
    
    return False

def minimax(board, current_player, depth, alp, bet):
    if(depth == 0 or game_over(board) == True or len(possible_moves(board, current_player)) == 0):
        return score(board)

    emptList = possible_moves(board, current_player)
    
    if(current_player == 'x'):
        value = float('-inf')
        for empty in emptList:
            new_board = make_move(board, 'x', empty)
            value = max(value, minimax(new_board, 'o', depth - 1, alp, bet))

            alp = max(alp, value) 

            if(value >= bet):
                break

        return value

    if(current_player == 'o'):
        value = float('inf')
        for empty in emptList:
            new_board = make_move(board, 'o', empty)
            value = min(value, minimax(new_board, 'x', depth - 1, alp, bet))

            bet = min(bet, value)

            if(value <= alp):
                break
     
        return value

def find_next_move(board, current_player, depth):
    list_poss = []
    alp = float('-inf')
    bet = float('inf')

    if(current_player == 'x'):
        list_poss = [(minimax(make_move(board, current_player, i), 'o', depth, alp, bet), i) for i in (possible_moves(board, current_player))] 
        print(list_poss)
        return max(list_poss, key=lambda a:a[0])[1]

    else:
        list_poss = [(minimax(make_move(board, current_player, i), 'x', depth, alp, bet), i) for i in (possible_moves(board, current_player))] 
        print(list_poss)
        return min(list_poss, key=lambda a:a[0])[1]

class Strategy():
    logging = True  # Optional
    def best_strategy(self, board, player, best_move, still_running):
        depth = 1

        for count in range(board.count(".")):  # No need to look more spaces into the future than exist at all
            print(depth)
            best_move.value = find_next_move(board, player, depth)
            print(best_move.value)
            depth += 1