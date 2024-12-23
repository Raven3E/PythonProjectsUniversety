def print_params(a=1, b='строка', c=True):
    print(a, b, c)

    #вызову функции с разным количеством аргументов
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
print_params(42, 'новая строка', False)

    # Распаковка параметров
values_list = [42, 'example', False]
values_dict = {'a': 100, 'b': 'текст', 'c': True}

    #Распаковка списка
print_params(*values_list)
     # Распакова словаря
print_params(**values_dict)
     # Распаковка + отдельные параметры
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)