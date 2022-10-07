'''задача 1. Задайте натуральное число N. 
Напишите программу, которая составит список простых множителей числа N.'''

import json
import os
clear = lambda: os.system('clear')
clear()

print("\n***Программа разложение числа N на простые множители***")

fname='natural_number.json' #открываем файл
with open(fname, 'r', encoding='utf-8') as fh:  # открываем файл на чтение
    BD_local = json.load(fh)  # загружаем из файла данные в словарь data

def decomposition (d):
    a=[]

    for i in range(d):
        if d==1:
            break
        while d%BD_local[i]==0:
            s=d/BD_local[i]
            a.append(BD_local[i])
            d=s
            
    return a

try:
    d=int(input("\nВведите целое число: "))
    print(decomposition(d))
except:
    print("\nНужно вводить число!")