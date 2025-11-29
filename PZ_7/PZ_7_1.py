#Вариант 22. Дана строка, изображающая целое положительное число. Вывести сумму цифр этого числа.

import random

num = str (random.randint(1, 50))
print (num)
s = 0
for i in num:
    s = s + int (i)
print (s)