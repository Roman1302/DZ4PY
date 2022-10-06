'''задача 3. Задана натуральная степень k. 
Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
многочлена и записать в файл многочлен степени k.
*Пример:* 
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0'''

import os
import json

clear = lambda: os.system('clear')
clear()

indexes = {"0": "\u2070",
           "1": "\u00B9",
           "2": "\u00B2",
           "3": "\u00B3",
           "4": "\u2074",
           "5": "\u2075",
           "6": "\u2076",
           "7": "\u2077",
           "8": "\u2078",
           "9": "\u2079"
           }

print("\n***Программа записи результата многочлена***")

k=int(input("Введите натуральную степень k: "))

from random import randint
def random(k):
    a,b = 0, 10
    lst = [None] * (k+1)
    for i in range(k+1):
        lst[i] = randint(a,b)
    return lst

a=random(k)
# print(a)

def degree(k):
    c=[]
    for i in range(2, k+1):
        degrees = ""
        # print("i", i)
        temp = str(i)
        for char in temp:
            degrees += indexes[char] or ""
        c.append(degrees)
        # print("de", degrees)
    return c
c=degree(k)
# print("c", c)


b=[]
for i in range(k+1):
    if a[i]>1 and k-i>1:
        n=str(a[i])+"*x"+str(c[-i-1])
        b.append(n)
        # b.append("*x")
        # b.append(k-i)
        # b.append("+")
    elif a[i]==1 and a[k]>1:
        n="x"+str(c[-i-1])
        b.append(n)
        # b.append("+")
    elif a[i]>1 and k-i==1:
        n=str(a[i])+"*x"
        b.append(n)
    elif a[i]==1 and k-i==1:
        b.append("x")
        # b.append("+")
    # elif a[i]==1 and k-i==1:
    #     b.append("x")
    #     # b.append("+")
    # elif a[i]==0 and k-i==0:
    #     b.append("=0")
    elif a[i]>0 and k-i==0:
        n=str(a[i])
        b.append(n)
    #     b.append("=0")
        
# print(*b, sep=" + ", end=" = 0\n")


my_lst = b
my_lst_str = ' + '.join(my_lst) + " = 0"
# print(my_lst_str)

def load():
            # загрузить из json
            fname='multinomial.json' #открываем файл
            with open(fname, 'r', encoding='utf-8') as fh:  # открываем файл на чтение
                BD_local = json.load(fh)  # загружаем из файла данные в словарь data
            # print('БД успещно загружена')
            return BD_local
def save():
    # сохранить в json
    with open('multinomial.json', 'w', encoding='utf-8') as fh:  # открываем файл на запись
        fh.write(json.dumps(my_lst_str,
                    ensure_ascii=False))  # преобразовываем словарь data в unicode-строку и записываем в файл
    # print('БД успещно сохранена')
save()
BDnew = load ()
print(BDnew)
