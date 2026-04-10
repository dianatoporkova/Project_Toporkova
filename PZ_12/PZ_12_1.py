#Вариант 22. В матрице найти минимальный элемент в предпоследнем столбце.

import random
n = int (input ('Введите размер матрицы: '))
m = [[random.randint(1, 100) for i in range(n)] for j in range(n)]
print (m)
z = min(map(lambda i: i[-2], m))
print ('Минимальный элемент:', z)