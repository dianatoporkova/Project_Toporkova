#Вариант 22. Из предложенного текстового файла (text18-22.txt) вывести на экран его содержимое, количество букв в
#верхнем регистре. Сформировать новый файл, в который поместить текст в стихотворной форме
#предварительно заменив символы третей строки их числовыми кодами.

file = open('text18-22.txt', 'r', encoding='utf-16')
k = file.readlines()
file.close()
print('Содержимое исходного файла:')
for i in range(len(k)):
    print(k[i].rstrip())
m = 0
for i in range(len(k)):
    for j in range(len(k[i])):
        if k[i][j].isupper():
            m += 1
print('Количество букв в верхнем регистре:', m)
if len(k) >= 3:
    n = []
    for i in range(len(k)):
        n.append(k[i])
    third_line = k[2].rstrip('\n')
    c = ''
    for j in range(len(third_line)):
        c += str(ord(third_line[j])) + ' '
    n[2] = c + '\n'
    file2 = open('text18-22_new.txt', 'w', encoding='utf-16')
    for i in range(len(n)):
        file2.write(n[i])
    file2.close()