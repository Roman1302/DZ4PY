''''задача 2 . Задайте последовательность чисел. Напишите программу, 
которая выведет список неповторяющихся элементов исходной последовательности.'''

import os
clear = lambda: os.system('clear')
clear()

print("\n***Программа выведет список неповторяющихся элементов***")

from random import randint
def random(list_length, ranger):
    a,b = int(ranger[0]), int(ranger[1])
    lst = [None] * list_length
    for i in range(list_length):
        lst[i] = randint(a,b)
    return lst

def sort(lst):  
    swapped = True
    while swapped:
        swapped = False
        # print(len(lst))
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True
    return lst

def unique_number(lst):
    list_of_unique_numbers = []
    unique_numbers = set(lst)

    for lst in unique_numbers:
        list_of_unique_numbers.append(lst)

    return list_of_unique_numbers


try:
    list_length=int(input("Введите длиту последовательных числе: "))
    ranger = input("Введите диапазон случайных числе через пробел: ").split()

    a=random(list_length, ranger)
    print(a)
    b=sort(a)
    # print(b)
    unique_number(b)
    print(unique_number(b))
except:
    print("\nНужно вводить число!")


