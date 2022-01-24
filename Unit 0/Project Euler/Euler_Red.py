import sys

# Red Credit Option #1

# Problem 17

def problem_17():
    ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    num_letters = 0
    num_ones = 0
    num_tens = 0
    num_teens = 0

    for one in ones:
        num_ones = num_ones + len(one)
        num_letters = num_letters + len(one)    # 1-9

    for ten in tens:
        num_tens = num_tens + len(ten)

    for teen in teens:
        num_teens = num_teens + len(teen)
        num_letters = num_letters + len(teen)   # 10-19

    num_letters = num_letters + (8 * num_ones) + (10 * num_tens)    # 20-99
    num_1_99 = num_letters

    num_letters = num_letters + (100 * num_ones)   # to account for "one" hundred, "two" hundred
    num_letters = num_letters + (9 * num_1_99)     # for each set of hundreds, 9 times
    num_letters = num_letters + (9 * 7)            # to account for 9 hundreds
    num_letters = num_letters + (891 * 10)         # to account for 891 "hundred and"
    num_letters = num_letters + 11                 # to account for the length of "one thousand"

    print("17:" ,str(num_letters))  # 21124

problem_17()

# Problem 21

def divisor_list(x):
    list_div = [1]
    num = 2
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

    return sum(list_div)

sum_amicable = 0

for i in range(220, 10000):
    num1 = divisor_list(i)
    num2 = divisor_list(num1)

    if((num2 == i) and (num1 != num2)):
        sum_amicable = sum_amicable + num1 + num2

print("21:", int(sum_amicable / 2))


# Problem 28

sum = 1

for i in range(1, 501):
    sum = sum + (4 * ((1 + (2 * i)) ** 2))
    sum = sum - (6 * (2 * i))

print("28:", sum)      # 669171001

# Problem 30

def fifth_power(x):
    sum = 0
    num = str(x)

    for elem in num:
        sum = sum + (int(elem) ** 5)
    
    if(sum == x):
        return True

    else:
        return False
    
sum_fifth = 0

for i in range(2, 400000):
    check = fifth_power(i)

    if(check == True):
        sum_fifth = sum_fifth + i

print("30:", sum_fifth)        # 443839

# Problem 12

def num_divisors(x):
    num = 2
    sq_rt = x ** 0.5
    iter = 2

    while(iter <= sq_rt):
        if(x % iter == 0):
            if(iter == sq_rt):
                num += 1
                break
            
            else:
                num += 2

        iter += 1

    return num

triangle_nums = [1]
bool = False
iter = 2

while(bool == False):
    sum = triangle_nums[iter - 2] + iter
    triangle_nums.append(sum)

    num_div = num_divisors(sum)

    if(num_div > 500):
        print("12:", sum)          # 76576500
        bool = True

    iter += 1


# Problem 14

nums_chains = {}

for i in range(2, 1000000):
    len = 1
    curr_num = i
    
    while(curr_num != 1):
        if(curr_num % 2 == 0):
            curr_num /= 2
        
        else:
            curr_num = (curr_num * 3) + 1
        
        len += 1
    
    nums_chains[i] = len

s_nums_chains = sorted(nums_chains.items(), key=lambda x: x[1])         # Inspiration from this line of code obtained from: https://www.geeksforgeeks.org/ways-sort-list-dictionaries-values-python-using-lambda-function/
item = s_nums_chains[999997]
print("14:", item[0])      # 837799