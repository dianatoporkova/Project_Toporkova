#Вариант 22. Описать функцию Mean(X, Y, AMean, GMean), вычисляющую среднее арифметическое
#AMean = (X+Y)/2 и среднее геометрическое GMean = у/Х У двух положительных чисел
#X и Y (X и У — входные, AMean и GMean - выходные параметры вещественного типа). С помощью этой функции
#найти среднее арифметическое и среднее геометрическое для пар (А, В), (А, С), (А, D), если даны A, B, C, D.

import math

def Mean (X, Y):
    AMean = (X + Y) / 2
    GMean = math.sqrt(X * Y)
    return AMean, GMean

try:
    A = float (input ("Введите число A: "))
    B = float (input ("Введите число B: "))
    C = float (input ("Введите число C: "))
    D = float (input ("Введите число D: "))
    if A <= 0 or B <= 0 or C <= 0 or D <= 0:
        print ("Ошибка. Число должно быть положительным.")
    else:
        AMean1, GMean1 = Mean (A, B)
        print (AMean1, "и", GMean1)
        AMean2, GMean2 = Mean (A, C)
        print(AMean2, "и", GMean2)
        AMean3, GMean3 = Mean (A, D)
        print (AMean3, "и", GMean3)
except ValueError:
    print ("Ошибка. Попробуй ввести число.")