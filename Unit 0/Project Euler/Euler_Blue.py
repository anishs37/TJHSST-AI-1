# Name: Anish Susarla
# Date: 8/26/2021

# Problems Done: 1, 2, 3, 4, 5, 6, 7, 8, 9, 29

import sys

# is_prime function

def is_prime(x):
    max_check = int(x ** 0.5) + 1

    if((x % 2 == 0) and x != 2):
        return False
    
    for i in range(3, max_check, 2):
        if(x % i == 0):
            return False
    
    return True


# Problem 1

print(sum(list(i * 3 for i in range(334))) + sum(list(i * 5 for i in range(200))) - sum(list(set(list(i * 3 for i in range(334))).intersection(list(i * 5 for i in range(200))))))    #233168 - One Liner

# Code is getting multiples of 3 and 5, and adding those items to a list and getting the sum. Then, the code is getting the sum of the numbers that is a multiple of both 3 and 5 and subtracting that from the previous sum.


# Problem 2

fib_list = [1, 2]
iter = 0

while(all(i <= 4000000 for i in fib_list)):
    fib_list.append(fib_list[iter] + fib_list[iter + 1])
    iter = iter + 1

sum = 0

for i in fib_list:
    if(i % 2 == 0):
        sum = sum + i

print(sum)                      # 4613732


# Problem 3

def prime_factor(x):
    highest_factor = int(x ** 0.5)

    for i in range(highest_factor, 1, -1):
        if(x % i == 0 and is_prime(i)):
            return i
    
    return 1

print(prime_factor(600851475143))       # 6857


# Problem 4

palin_list = []

for i in range(100, 1000):
    for j in range(100, 1000):
        prod = i * j
        str_prod = str(prod)
        
        if(str_prod[::1] == str_prod[::-1]):
            palin_list.append(prod)

print(max(palin_list))      # 906609


# Problem 5

def gcd(x, y):
    if(y == 0):
        return x
    
    else:
        return gcd(y, x % y)

iter = 20
numCount = 0
bool = False

while(bool == False):
    for i in range(20, 1, -1):
        gcd_num = gcd(iter, i)
        
        if(gcd_num == i):
            numCount = numCount + 1
        
        else:
            iter = iter + 20
            numCount = 0

        if(numCount == 19):
            bool = True
            print(iter)             # 232792560
        

# Problem 6

sum_squares = []
nums = []

for i in range(1, 101):
    sum_sq = i ** 2
    sum_squares.append(sum_sq)
    nums.append(i)

sum = 0
sum2 = 0

for i in sum_squares:
    sum = sum + i

for i in nums:
    sum2 = sum2 + i

sum_nums_sq = sum2 ** 2
print(sum_nums_sq - sum)        # 25164150


# Problem 7

count = 0
num = 2

while count < 10001:
    if(is_prime(num)):
        count = count + 1

    num = num + 1

print(num - 1)                      #104743


# Problem 8

num = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
iter = 0
num_dict = {}

while(iter <= 987):
    num1 = num[iter]
    num2 = num[iter + 1]
    num3 = num[iter + 2]
    num4 = num[iter + 3]
    num5 = num[iter + 4]
    num6 = num[iter + 5]
    num7 = num[iter + 6]
    num8 = num[iter + 7]
    num9 = num[iter + 8]
    num10 = num[iter + 9]
    num11 = num[iter + 10]
    num12 = num[iter + 11]
    num13 = num[iter + 12]
    prod = int(num1) * int(num2) * int(num3) * int(num4) * int(num5) * int(num6) * int(num7) * int(num8) * int(num9) * int(num10) * int(num11) * int(num12) * int(num13)
    str_num = str(num1) + str(num2) + str(num3) + str(num4) + str(num5) + str(num6) + str(num7) + str(num8) + str(num9) + str(num10) + str(num11) + str(num12) + str(num13)
    num_dict[str_num] = prod
    iter = iter + 1

max_key = max(num_dict, key = num_dict.get)
prod = 1

for i in range(len(max_key)):
    int_index = int(max_key[i])
    prod = prod * int_index

print(prod)                 # 23514624000


# Problem 9

def is_pythag(a, b, c):
    a_sq = a ** 2
    b_sq = b ** 2
    c_sq = c ** 2

    if(a_sq + b_sq == c_sq):
        return True
    
    return False

for a in range(1, 500):
    for b in range(1, 500):
        c = 1000 - a - b

        if(a < b < c):
            if(is_pythag(a, b, c)):
                print(a*b*c)


# Problem 29

val_set = {"0"}

for i in range(2, 101):
    for j in range(2, 101):
        num = i ** j
        val_set.add(str(num))

print(len(val_set) - 1)         # 9183