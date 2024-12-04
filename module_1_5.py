immutable_var = ("Tigran", "Python", "Urban", 2024, True)
print("Immutable tuple:", immutable_var)

# immutable_var[0] = 100
# Кортежи неизменияими!!

mutable_list = [1, 2, 'a', 'b']
print("Оригинал:", mutable_list)
mutable_list[2] = "T"
mutable_list.append('Обновление')
print("Обновление:", mutable_list)
