# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
list1 = [1, 2, 3, 4.1]
list2 = [1, 2, 3, 4.1]
list3 = ['a', None, True, []]

list1.insert(0, [1, 2]) # добавляет в любое место списка элемент
# list1.clear()
list4 = list1.copy() # или через полный срез


print(list1.count(1)) 
print(list1)
print(list2)
print(list3)
