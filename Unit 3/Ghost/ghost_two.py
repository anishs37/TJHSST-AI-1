import sys
min_length = int(sys.argv[2])
try: initial_word = sys.argv[3].lower()
except IndexError: initial_word = ''
with open(sys.argv[1]) as f: words = {line.strip().lower() for line in f if len(line.strip()) >= min_length and line.strip().isalpha}
sub_sets = {i:{j[0:i] for j in words if len(j) >= i} for i in range(1, len(max(words, key=len))+1)}
def possible_moves(word): return [i for i in 'abcdefghijklmnopqrstuvwxyz' if word+i in sub_sets[len(word)+1]]
def check_game_over(word, player): return 1 if word in words else None
def negamax(word, player, alpha, beta):
    if check_game_over(word, player) != None: return check_game_over(word, player)
    value = float('-inf')
    for i in possible_moves(word): 
        value = max(value, -1*negamax((word+i), not player, -beta, -alpha))
        alpha = max(alpha, value)
        if alpha >= beta: return value
    return value
def find_next_move(word, player): return [(-1*negamax(word+i, not player, float('-inf'), float('inf')), i) for i in possible_moves(word)]
print(f'Next player can guarantee victory by playing any of these letters: {[i[1].upper() for i in find_next_move(initial_word, True) if i[0] == 1]}') if [i[1] for i in find_next_move(initial_word, True) if i[0] == 1] else print('Next player will lose!')