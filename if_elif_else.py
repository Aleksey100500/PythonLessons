# if - Elif - else
# если больше 3х вложенностей приссутствует в программе, то нужно идти через декомпоицию
temp = 14 # temperature

# if temp < 10:
#     print('холодно')
# elif 10 <= temp < 28:
#     if 10 <= temp < 15:
#         print('холодно, но нормально')
#     else:
#         print('очень жарко, но нормально')
# else:
#     print('очень жарко')

# тернарные операции

result = 'Holodno' if temp < 10 else "Teplo"
print(result)