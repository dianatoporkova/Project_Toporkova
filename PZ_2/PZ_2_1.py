try:
    num = int (input ("Введите число большее 999: "))
    if num <= 999:
        print ("Ошибка: число должно быть больше 999")
    else:
        hund = (num // 100) % 10
        print (hund)
except ValueError:
    print ("Ошибка. Попробуй ввести число.")