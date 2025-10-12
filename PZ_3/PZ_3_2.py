#Вариат 22. Даны два числа. Вывести большее из них.

try:
    num1 = int (input ('Введите первое число: '))
    num2 = int (input ('Введите второе число: '))
    if num1 > num2:
        print (num1)
    elif num1 < num2:
        print (num2)
except ValueError:
    print ('Ошибка. Попробуй ввести число.')