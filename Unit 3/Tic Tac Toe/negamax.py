import sys
import time

def print_board(board):
    str_to_print = ""
    iter = 1

    for elem in board:
        str_to_print = str_to_print + elem

        if(iter % 3 == 0):
            str_to_print = str_to_print + '\t' + str(iter -3) + str(iter - 2) + str(iter - 1)
            str_to_print = str_to_print + '\n'

        iter = iter + 1

    print(str_to_print)

def game_over(board):
    if(board[0:3] == 'XXX' or board[3:6] == 'XXX' or board[6:9] == 'XXX'):
        return (True, 1)

    if(board[0:7:3] == 'XXX' or board[1:8:3] == 'XXX' or board[2:9:3] == 'XXX'):
        return (True, 1)

    if(board[0:9:4] == 'XXX' or board[2:7:2] == 'XXX'):
        return (True, 1)
    
    if(board[0:3] == 'OOO' or board[3:6] == 'OOO' or board[6:9] == 'OOO'):
        return (True, -1)
        
    if(board[0:7:3] == 'OOO' or board[1:8:3] == 'OOO' or board[2:9:3] == 'OOO'):
        return (True, -1)

    if(board[0:9:4] == 'OOO' or board[2:7:2] == 'OOO'):
        return (True, -1)
    
    if(board.find('.') == -1):
        return (True, 0)

    return (False, 0)

def game_over_1(board):
    if(board[0:3] == 'XXX' or board[3:6] == 'XXX' or board[6:9] == 'XXX'):
        return (True, -1)

    if(board[0:7:3] == 'XXX' or board[1:8:3] == 'XXX' or board[2:9:3] == 'XXX'):
        return (True, -1)

    if(board[0:9:4] == 'XXX' or board[2:7:2] == 'XXX'):
        return (True, -1)
    
    if(board[0:3] == 'OOO' or board[3:6] == 'OOO' or board[6:9] == 'OOO'):
        return (True, 1)
        
    if(board[0:7:3] == 'OOO' or board[1:8:3] == 'OOO' or board[2:9:3] == 'OOO'):
        return (True, 1)

    if(board[0:9:4] == 'OOO' or board[2:7:2] == 'OOO'):
        return (True, 1)
    
    if(board.find('.') == -1):
        return (True, 0)

    return (False, 0)

def possible_next_boards(board, current_player):
    list_possible = []

    index = 0

    for elem in board:
        if(elem == '.'):
            str_to_add = board[:index] + current_player + board[index + 1:]
            list_possible.append(str_to_add)
        
        index = index + 1
    
    return list_possible

def negamax(board, token):
    if(token == 'X'):
        game_condition, score = game_over(board)
    
    else:
        game_condition, score = game_over_1(board)

    if(game_condition == True):
        return score
    
    results = []

    for next_board in possible_next_boards(board, token):

        if(token == 'X'):
            results.append(-1 * negamax(next_board, 'O'))
        
        else:
            results.append(-1 * negamax(next_board, 'X'))
    
    return max(results)

def empty_spaces(board):
    list_empty = []
    index = 0

    for elem in board:
        if(elem == '.'):
            list_empty.append(index)
        
        index = index + 1
    
    return list_empty

def string_representation(list_empty):
    str_to_ret = ''
    lenList = len(list_empty)

    for index, value in enumerate(list_empty):
        if(index != lenList - 1):
            str_to_ret = str_to_ret + str(value) + ', '
        
        else:
            str_to_ret = str_to_ret + str(value)
    
    return str_to_ret

def change_board(board, ind):
    toMove = 'O'

    if(current_player == 'O'):
        toMove = 'X'
    
    board = board[:ind] + toMove + board[ind + 1:]

    return board

def ai_play(board, emptList):
    list_scores = []
    if(current_player == 'X'):
        for empty in emptList:
            new_board = board[:empty] + current_player + board[empty + 1:]
            score = negamax(new_board, 'O')
            list_scores.append((empty, score))

            if(score == -1):
                print("Moving at " + str(empty) + " results in a win.")
            
            if(score == 0):
                print("Moving at " + str(empty) + " results in a tie.")
            
            if(score == 1):
                print("Moving at " + str(empty) + " results in a loss.")
        
        print("")
        
        min_y = 2
        min_y_ind = -1

        for x, y in list_scores:
            if(y < min_y):
                min_y = y
                min_y_ind = x
        
        print("I choose space " + str(min_y_ind) + ".")
        next_board_2 = board[:min_y_ind] + "X" + board[min_y_ind + 1:]
        return next_board_2
    
    if(current_player == 'O'):
        for empty in emptList:
            new_board = board[:empty] + current_player + board[empty + 1:]
            score = negamax(new_board, 'X')
            list_scores.append((empty, score))

            if(score == -1):
                print("Moving at " + str(empty) + " results in a win.")
            
            if(score == 0):
                print("Moving at " + str(empty) + " results in a tie.")
            
            if(score == 1):
                print("Moving at " + str(empty) + " results in a loss.")
        
        print("")

        min_y = 2
        min_y_ind = -1

        for x, y in list_scores:
            if(y < min_y):
                min_y = y
                min_y_ind = x
        
        print("I choose space " + str(min_y_ind) + ".")
        next_board_2 = board[:min_y_ind] + "O" + board[min_y_ind + 1:]
        return next_board_2

#current_board = sys.argv[1]
current_board = sys.argv[1]

if(current_board.count('.') == 9):
    current_player = input("Should I be X or O? ")

    if(current_player == 'X'):
        playIter = 0
    
    else:
        playIter = 1

else:
    num_x = current_board.count('X')
    num_o = current_board.count('O')

    if(num_x == num_o):
        current_player = 'X'
        playIter = 0
    
    else:
        current_player = 'O'
        playIter = 0

while(game_over(current_board)[0] == False):
    print('')
    print('Current board:')
    print_board(current_board)

    list_empty = empty_spaces(current_board)

    if(playIter % 2 == 0):
        player_playing = current_player
        next_board = ai_play(current_board, list_empty)
        current_board = next_board
    
    else:
        if(current_player == 'X'):
            player_playing = 'O'
        
        else:
            player_playing = 'X'

        str_rep = string_representation(list_empty)
        print("You can move to any of these spaces: " + str_rep + ".")
        spaceMove = int(input("Your choice? "))
        next_board = change_board(current_board, spaceMove)
        current_board = next_board

    playIter = playIter + 1

print('')

print('Current board:')
print_board(current_board)

end_state, end_result = game_over(current_board)

if(end_result == 0):
    print("We tied!")

elif(end_result == 1):
    if(current_player == 'X'):
        print("I win!")
    
    else:
        print("You win!")

else:
    if(current_player == 'X'):
        print("You win!")
    
    else:
        print("I win!")