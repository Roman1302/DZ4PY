'''задача 4. Задайте два числа. Напишите программу, которая найдёт НОК 
(наименьшее общее кратное) этих двух чисел.'''

import os

clear = lambda: os.system('clear')
clear()

print("\n*** Программа поиска НОК двух чисел ***")
n=[]
n=input("Введите два целых числа через пробел: ").split()

print(n)

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
print(a)
b=[]
b=prime_factors(int(n[1]))
print(b)

def op(a, b):
    # ints_list = a 
    # temp = [] 
    # while result!="":
    #     for x in ints_list: 
    #         if x not in temp: 
    #             temp.append(x) 
    #             ints_list = temp 
    #             print(f'Updated List after removing duplicates = {temp}')
        result=list(set(a) & set(b))
        print(result)
        a.remove(result[0])
        print(a)
        return a

op(a,b)
print(op(a,b))

v = a + b
print(v)

import functools
print (functools.reduce(lambda a, b : a * b, v))


# ints_list = a 
# temp = [] 
# for x in ints_list: 
#     if x not in temp: 
#         temp.append(x) 
#         ints_list = temp 
#         print(f'Updated List after removing duplicates = {temp}')

# result=list(set(a) & set(b))
# print(result)
# a.remove(result[0])
# print(a)

# ints_list = a 
# temp = [] 
# for x in ints_list: 
#     if x not in temp: 
#         temp.append(x) 
#         ints_list = temp 
#         print(f'Updated List after removing duplicates = {temp}')

# result=list(set(a) & set(b))
# print(result)
# a.remove(result[0])
# print(a)
