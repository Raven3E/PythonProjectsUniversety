my_dict = {'Vasya': 1975, 'Egor': 1999, 'Masha': 2002}
print("Исходный словарь", my_dict)
existing_value = my_dict.get('Masha')
print("Значение ключа", existing_value)
non_existing_value = my_dict.get('Ivan')
print("значение отсутствует", non_existing_value)
my_dict['Kamila'] = 1981
my_dict['Artem'] = 2015
deleted_value = my_dict.pop('Egor')
print("Удаленное значение:", deleted_value)
print(my_dict)

my_set = {1, '<Banan', 55.88, 228, 'apple', (5, 6, 8.5)}
print(my_set)
my_set.add(13)
my_set.add('Python')
my_set.remove('apple')
print(my_set)
