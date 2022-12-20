# print('= Модицикация регистра=')
# target = 'Python: Быстрый старт!'

# print(target.lower())
# print(target.upper())
# print(target.capitalize()) #только первую букву делает верхнего регистра
# print(target.title()) #все первые буквы слов к верхнему
# print(target.swapcase()) # менякт все нижнего к верхнему и наоборот

# print('= Удаление лишнего =')
# word = '  ...,,,hello?....  '

# print(word.strip()) # удалит пробелы
# print(word.strip('.! ,?')) # удалит символы указанные в методе
# print(word.lstrip()) # удалит символы от слова слева
# print(word.rstrip()) # справа

# print('Проверка строк')
# target = 'Alpha12'

# print(target.isalnum()) # проверяет на наличие букв и символов
# print(target.isalpha())# на буквы
# print(target.islower())# все буквы являются прописными
# print(target.istitle())# все слова с большой буквы?
# print(target.isdigit())# проверяет на элемент цифру

# print('Модификаторы длины')
# a = 'test'
# b = 'some long test string'
# c = '10.00'

# print(a.zfill(10)) # заполняет нулями слева строку на разницу между длиной строки и 10, если текущая длина строки меньше 10
# print(b.zfill(10))
# print(c.zfill(10))

# print(a.center(10, ' ')) #центрует строку заполняя пустоты символов в скобках, символом может быть любой символ

# print('Методы поиска')
# target = 'Python: Быстрый старт!'

# print(target.endswith('арт', 0, -1)) # выдает тру если то что мы ищем в конечном слове есть в строке
# print(target.startswith('Pyt', 0, -1))
# print('Python' in target)
# print(target.find('Быстрый')) # выдает индекс начала искомого слова в строке
# print(target.index('старт')) # 

print(' Еще больше полезных методов ')
TARGET = 'Python: Быстрый старт!'

print(TARGET.replace('т', 'ТТТ', 1))# заменяет символы строки

table = TARGET.maketrans('PБ:', 'GB;')
print(TARGET.translate(table))

print(TARGET.split())
print(list(TARGET))

print(TARGET.partition('Быстрый'))

l = ['П', 'р', 'и', 'в', 'е', 'т']
print('*'.join(l))