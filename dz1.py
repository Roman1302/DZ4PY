'''задача 1. Задайте натуральное число N. 
Напишите программу, которая составит список простых множителей числа N.'''
import json
import os
clear = lambda: os.system('clear')
clear()

print("\n***Программа разложение числа N на простые множители***")
natural_number=int(input("\nВведите целое число: "))

fname='natural_number.json' #открываем файл
with open(fname, 'r', encoding='utf-8') as fh:  # открываем файл на чтение
    BD_local = json.load(fh)  # загружаем из файла данные в словарь data
# print('БД успещно загружена')

# print(BD_local[0])


a=[]

for i in range(natural_number):
    if natural_number==1:
         break
    # print("до", natural_number/BD_local[i])
    while natural_number%BD_local[i]==0:
        s=natural_number/BD_local[i]
        # print("s",s)
        # print(BD_local[i])
        a.append(BD_local[i])
        # print("a",a)
        natural_number=s
        # print("natural_number", natural_number)
        # print("natural_number/BD_local[i]",s/BD_local[i])
print(a)
