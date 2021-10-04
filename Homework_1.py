""" Digit Sum 3 """
user_input = int(input("Please write your number: "))
digits = 0
first = user_input // 100
last = user_input % 10
second = user_input//10 % 10
digits+= first +last +second
print(digits)

""" Triangle """
first_side  = int(input())
second_side = int(input())
area =  (first_side * second_side) * 0.5
print(area)

""" Arithmetic Progression """
a_1 = int(input())
a_2 = int(input())
n = int(input())
d = a_2 - a_1
a_n = a_1 + (n-1)*d
print(a_n)

""" Century from year """
year_input = int(input("Year: "))
century = (year_input + 99)//100
print(century)

""" Two men """
first_man = int(input())
second_man  = int(input())
shots = first_man + second_man - 1
first_out = shots - first_man
second_out = shots - second_man
print(first_out, second_out)

""" Knight move"""
x = int(input())
y = int(input())
x1, y1 = x + 1, y - 2
x2, y2 = x - 1, y - 2
x3, y3 = x + 1, y + 2
x4, y4 = x - 1, y + 2
x5, y5 = x + 2, y + 1
x6, y6 = x + 2, y - 1
x7, y7 = x - 2, y + 1
x8, y8 = x - 2, y - 1
print(x1, y1)
print(x2, y2)
print(x3, y3)
print(x4, y4)
print(x5, y5)
print(x6, y6)
print(x7, y7)
print(x8, y8)

