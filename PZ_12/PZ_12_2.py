#Вариант 22. Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее элементов.

n = int (input ('Введите размер матрицы: '))
m = [[j * n + i for i in range(n)] for j in range(n)]
print (m)
v = [m[i] for i in range(n) if (i + 1) % 2 != 0]
a = list (map (lambda i: sum (i) / len (i), v))
print('Среднее арифметическое для строк с нечетным номером:', a)