my_string = input("Введите текст: ")
print("Количество символов:", len(my_string))
print("Верхний регистр:", my_string.upper())
print("Нижний регистр:", my_string.lower())
no_spaces = my_string.replace(" ", "")
print("Строка без пробелов:", no_spaces)
print("Первый символ:", my_string[0])
print('Последний символ:', my_string[-1])