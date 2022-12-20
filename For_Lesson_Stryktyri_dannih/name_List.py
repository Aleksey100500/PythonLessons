# Тема: Структуры Данных

list1 = [1, 2, 3, 4.1]
list2 = ['a', None, True ]
string = 'string'

# print(len(list1))

list2[0] = 'b'
list1.append(1)

print(list1[-1])
print(list2[0])
print(string[-1])
print(list1[0: len(list1)])

# Списки передаются по ссылкам

list3 = list1

list3.append(1)
list3.append(1)
list3.append(1)
print(id(list3), id(list1))

