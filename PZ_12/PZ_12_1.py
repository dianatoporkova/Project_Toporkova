#Вариант 22. В матрице найти минимальный элемент в предпоследнем столбце.

n = int (input ('Введите размер матрицы: '))
m = [[j * n + i for i in range(n)] for j in range(n)]
print (m)
z = min(map(lambda i: i[-2], m))
print ('Минимальный элемент:', z)