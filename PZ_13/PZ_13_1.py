#Вариант 22. Из исходного текстового файла (ip_address.txt) из раздела «Частоупотребимые маски» перенести
#в первый файл строки с нулевым четвертым октетом, а во второй - все остальные.
#Посчитать количество полученных строк в каждом файле.

import re
with open('ip_address.txt', 'r', encoding='utf-8') as file:
    text = file.read()

m = re.search(r'Частоупотребимые маски\n(.*?)(?=\n\n|\Z)', text, re.DOTALL)

c = m.group(1)
s = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', c)
zero = [i for i in s if i.endswith('.0')]
other = [i for i in s if not i.endswith('.0')]
with open('zero.txt', 'w', encoding='utf-8') as file:
    file.write('\n'.join(zero))
with open('other.txt', 'w', encoding='utf-8') as file:
    file.write('\n'.join(other))
print('С нулевым четвертым октетом:', len(zero))
print('Остальные:', len(other))