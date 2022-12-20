# s = 'Python \"быстрый\" старт' #\\ этот символ escape нужен,, чтобы можно было выделить такими же ковычками как и выделяем мы текст

# s = r'Python\nбыстрый старт' #сырые строки - строки, в которых символы не обрабатываются а выводится всё как есть
# s = 'Python'
# print('Pyt' in s)

# 1 СПОСОБ ВВЕСТИ ИМЯ.
# name = input('Input name: ')
# s = 'Hello, %s %f' % (name, 10)

# print(s)

# 2. Через FORMAT
# name = input('Input name: ')
# s = 'Hello, {} {}'.format(name, 10)

# print(s)

# 3. Через f строки
name = input('Input name: ')
s = f'Hello, {name}'

print(s)