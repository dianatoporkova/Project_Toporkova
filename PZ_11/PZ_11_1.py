#Вариант 22. Даны текущие оценки студента по дисциплине «Основы программирования» за месяц.
#Необходимо найти количество «2», «3», «4» и «5», полученных студентом, и определить итоговую оценку за месяц.

from functools import reduce
marks = [2, 5, 5, 4, 3, 3]
marks_2 = len ([1 for i in marks if i == 2])
print('Двоек:', marks_2)
marks_3 = len ([1 for i in marks if i == 3])
print('Троек:', marks_3)
marks_4 = len ([1 for i in marks if i == 4])
print('Четвёрок:', marks_4)
marks_5 = len ([1 for i in marks if i == 5])
print('Пятёрок:', marks_5)
n = reduce (lambda x, y: x + y, marks)
print ('Итоговая оценка за месяц:', round (n / len (marks)))