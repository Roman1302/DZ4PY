# import json
# import os
# clear = lambda: os.system('clear')
# clear()

# print("\n***Программа разложение числа N на простые множители***")
# natural_number=int(input("\nВведите целое число: "))

# fname='natural_number.json' #открываем файл
# with open(fname, 'r', encoding='utf-8') as fh:  # открываем файл на чтение
#     BD_local = json.load(fh)  # загружаем из файла данные в словарь data
# # print('БД успещно загружена')

# # print(BD_local[0])


# a=[]

# for i in range(natural_number):
#     if natural_number==1:
#          break
#     # print("до", natural_number/BD_local[i])
#     while natural_number%BD_local[i]==0:
#         s=natural_number/BD_local[i]
#         # print("s",s)
#         # print(BD_local[i])
#         a.append(BD_local[i])
#         # print("a",a)
#         natural_number=s
#         # print("natural_number", natural_number)
#         # print("natural_number/BD_local[i]",s/BD_local[i])
# print(a)
   


# def eq(x, y, z):
#     return x ** 2 + y ** 2 + z ** 2
# lowerBound = int(input("Введите нижнюю границу поиска. "))
# upperBound = int(input("Введите верхнюю границу поиска. "))
# a = int(input("Введите свободный член x^2 + y^2 + z^2. "))
# for x in range(lowerBound, upperBound):
#     for y in range(lowerBound, upperBound):
#         for z in range(lowerBound, upperBound):
#             if (eq(x, y, z) == a):
#                 print("x=",x, end = ", ")
#                 print("y=", y, end = ", ")
#                 print("z=",z, end = " ")
# indexes = {"0": "\u2070",
#            "1": "\u00B9",
#            "2": "\u00B2",
#            "3": "\u00B3",
#            "4": "\u2074",
#            "5": "\u2075",
#            "6": "\u2076",
#            "7": "\u2077",
#            "8": "\u2078",
#            "9": "\u2079",
#            "-": "\u207B"
#            }


# def degree(digit: int, deg: int):
#     degrees = ""
#     temp = str(deg)
#     for char in temp:
#         degrees += indexes[char] or ""
#     return "a = " + str(digit) + degrees


# if __name__ == "__main__":
#     print(degree(1024, 56))
#     a, b = map(int, input("Введите число и степень: ").split())
#     print(degree(a, b))

# Задайте натуральное число N. Напишите программу, которая составит список
# простых множителей числа N.

# print('Программа составляющая список простых множителей числа N')
# num = int(input("Введите натуральное число N: "))
# i = 2 
# sp = []
# N = num
# while i <= num:
#     if num % i == 0:
#         sp.append(i)
#         num //= i
#         i = 2
#     else:
#         i += 1
# print(f"Для простых множителей числа N = {N} получился список : {sp}")

