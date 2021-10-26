# ------------THE GOLDBACH CONJECTURE-------------

def is_prime(num):
    for i in range(2, num//2+1):
        if num % i == 0:
            return False
    return True


def conjecture(num):
    for e in range(1, num//2+1):
        if is_prime(e) and is_prime(num - e):
            return e, num - e

num = int(input("Write number greater than 2: "))
print(conjecture(num))


# -------------------PALINDROME NUMBERS----------------

def is_palindrome(number):
    number_to_compare = number
    reversed_number = 0
    while number > 0:
        remainder = number % 10
        reversed_number = (reversed_number * 10) + remainder
        number = number//10
    if reversed_number == number_to_compare:
        return True
    return False

def pali_numbers(num_1, num_2):
    ls = []
    for i in range(num_1, num_2+1):
        if i < 10:
            ls.append(i)
        elif is_palindrome(i):
            ls.append(i)
    return ls

num_1 = int(input())
num_2 = int(input())
print(pali_numbers(num_1,num_2))



# ------------------------SUFFIX SUMS---------------------------

def suffix_sums(ls):
    sum_ls = []
    sums = 0
    for i in range(len(ls)):
        sums = sum(ls[i::])
        sum_ls.append(sums)
    return sum_ls

m = int(input())
ls = [float(input()) for _ in range(m)]
print(suffix_sums(ls))


# -----------------------CYCLIC SHIFT--------------------------

def cyclic_shift(seq, k):
    return seq[-k:] + seq[:-k]


# WOULD LIKE TO THINK OF A BETTER SOLUTION HERE :)

n = int(input())
seq = [int(input()) for _ in range(n)]
k = int(input())
print(cyclic_shift(seq, k))


#------------------------TREE-------------------------------

def tree(num):
    if num % 2 != 0:
        for symbol in range(1, num+1, 2):
            space = (num - symbol)//2
            print(space * ' ', symbol * '*')
    else:
        print('Please input odd number')

num = int(input())
tree(num)

