'''задача 4. Задайте два числа. Напишите программу, которая найдёт НОК 
(наименьшее общее кратное) этих двух чисел.'''

import os

clear = lambda: os.system('clear')
clear()

print("\n*** Программа поиска НОК двух чисел ***")
n=[]
n=input("Введите два целых числа через пробел: ").split()
A=n[0]
B=n[1]
# print(n)

def prime_factors(num):
    i = 2 
    sp = []
    N = num
    while i <= num:
        if num % i == 0:
            sp.append(i)
            num //= i
            i = 2
        else:
            i += 1
    return sp

a=prime_factors(int(n[0]))
# print(a)

b=prime_factors(int(n[1]))
# print(b)

def op(a, b):
    
    for i in range(len(a)):
        result=list(set(a) & set(b))
        # print("result", result)
        if not result:
            a
            # print("a", a)
        else:
            a.remove(result[0])

    return a

op(a,b)
# print(op(a,b))

# print("a", a)
v = op(a,b) + b
# print(v)

import functools
print ("НОК для ", A, "и", B, "=>", functools.reduce(lambda a, b : a * b, v))
