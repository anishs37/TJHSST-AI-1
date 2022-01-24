from collections import deque
import math
import time
import sys

dictionary = sys.argv[1]
puzzles = sys.argv[2]

start = time.perf_counter()
dict_word_children = {}

with open(dictionary) as f:
    dict_set = {line.strip() for line in f}

def get_children(word):
    children_list = []
    letters_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    iter = 0
    len_word = len(word)
    iter = 0

    while(iter < len_word):
        letterIter = 0
        for letter in letters_list:
            new_word = word[:iter] + letter + word[iter + 1:]

            if(new_word in dict_set and new_word != word):
                children_list.append(new_word)
            
            letterIter = letterIter + 1
        
        iter = iter + 1

    return children_list

for word in dict_set:
    list_children = get_children(word)
    dict_word_children[word] = list_children

end = time.perf_counter()
print("Time to create the data structure was: " + str(end - start) + " seconds")
print("There are " + str(len(dict_set)) + " words in this dict.")
print("")

with open(puzzles) as f:
    puzzle_list = [line.strip() for line in f]

def BFS(start_word, desired_word):
    fringe = deque()
    visited = {start_word}
    fringe.append((start_word, [start_word]))
    visited.add(start_word)

    while fringe:
        state, ancestors = fringe.popleft()

        if(state == desired_word):
            return ancestors, len(ancestors)
        
        else:
            children_list = dict_word_children[state]
            for c in children_list:
                if(c not in visited):
                    newAncestors = ancestors.copy()
                    newAncestors.append(c)
                    fringe.append((c, newAncestors))
                    visited.add(c)
    
    return [], 999999

start2 = time.perf_counter()

letters_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
iter3 = 0

for puzzle in puzzle_list:
    start_word, end_word = puzzle.split(" ")
    ancestorList, lenAncestors = BFS(start_word, end_word)

    if(lenAncestors != 999999):
        path = ancestorList
        
        print("Line: " + str(iter3))
        print("Length is: " + str(lenAncestors))

        for node in path:
            print(node)
     
        print("")
    
    else:
        print("Line: " + str(iter3))
        print("No solution!")
    
    iter3 = iter3 + 1

end2 = time.perf_counter()
print("")
print("Time to solve all of these puzzles was: " + str(end2 - start2) + " seconds") 
print("Total Time: " + str((end - start) + (end2 - start2)) + " seconds") 