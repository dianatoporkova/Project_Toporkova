#Вариант 22. 2.Из заданной строки отобразить только символы пунктуации. Использовать библиотеку string.
#Строка: --msg-template="$FileDir$\ {path}: {line}: {column}:{C}:({symbol}) {msg}"

from string import punctuation
msg_template = "$FileDir$\ {path}: {line}: {column}:{C}:({symbol}) {msg}"
n = [i for i in msg_template if i in punctuation]
print(n)