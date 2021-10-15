#-------------------------DIGIT PRODUCT---------------------

def digit_product(num):
    product = 1
    while num > 0:
        if num % 10 != 0:
            product*= num%10
            num //= 10
        num //= 10
    return product

num = int(input('Number: '))
print(digit_product(num))

#------------------------LARGEST POWER OF 3 ---------------

def largest_pow(num):
    power = num**(1/3)
    return int(power)

num = int(input('Number: '))
print(3**(largest_pow(100)))


#-----------------------------TRIANGLE -------------------

def triangle(a, b, c):
    if a + b <= c or c + b <= a or c + a <= b:
        print('No triangle')
    elif a == b == c:
        print('Acute Triangle')
    elif a**2 > b**2 + c**2 or b**2 > a**2 + c**2  or c**2 > a**2 + b**2:
        print('Obtuse Triangle')
    else:
        print('Right Triangle')

side_1 = float(input('Side 1: '))
side_2 = float(input('Side 2: '))
side_3 = float(input('Side 3: '))
triangle(side_1, side_2, side_3)

#----------------------THE ROOT OF THE NUMBER ------------

def root(num):
    sum_dig = 0
    while num > 0:
        sum_dig+=num%10
        num//=10
    while sum_dig >= 10:
        sum_dig = root(sum_dig)
    return sum_dig
num = int(input('Number: '))
print(root(num))


#--------------------NUMBER OF DIVISORS--------------------

def num_divisors(num):
    count = 0
    divisor = 1
    while divisor <= num:
        if num%divisor == 0:
            count+=1
        divisor +=1
    return count

num = int(input('Number: '))
print(num_divisors(num))


#-------------------QUADRATIC EQUATION --------------------

def quadratic(a,b,c):
    if a == 0:
        print('Non-quadratic equation')
        if b!=0:
            x_1 = -c/b
            print('One solution: ', x_1)
        elif c!=0:
            print('No solutions')
        else:
            print('Infinite Solutions')
    else:
        print('Quadratic equation')
        discr = b**2 - 4*a*c
        print('Discriminant: ', discr)
        if discr > 0:
            x_1 = (-b+ discr**(1/2))/(2*a)
            x_2 = (-b - discr**(1/2))/(2*a)
            print('Two Solutions: ', x_1, x_2)
        elif discr == 0:
            x_1 = (-b + discr ** (1 / 2)) / (2 * a)
            print('One Solution: ', x_1)
        else:
            print('No solutions')


a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
quadratic(a,b,c)