import sys

list_word = sys.argv[1:]
sep = "  "
word = sep.join(list_word)

print("#1: " + word[2])                                         #1
print("#2: " + word[4])                                         #2
print("#3: " + str(len(word)))                                  #3
print("#4: " + word[0])                                         #4
print("#5: " + word[len(word) - 1])                             #5
print("#6: " + word[len(word) - 2])                             #6
print("#7: " + word[3: 8])                                      #7
print("#8: " + word[len(word) - 5: len(word)])                  #8
print("#9: " + word[2:])                                        #9
print("#10: " + word[::2])                                      #10
print("#11: " + word[1::3])                                     #11
print("#12: " + word[::-1])                                     #12
print("#13: " + str(word.find(" ")))                            #13
print("#14: " + word[:len(word) - 1])                           #14
print("#15: " + word[1:len(word)])                              #15    
print("#16: " + word.lower())                                   #16
print("#17: " + str(word.split()))                              #17
print("#18: " + str(len(word.split())))                         #18
print("#19: " + str(list(word)))                                #19
print("#20: " + "".join(sorted(word)))                          #20
print("#21: " + word[0: word.find(" ")])                        #21
print("#22: " + str(word[::1] == word[::-1]))                   #22