class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for floor in range(1, new_floor + 1):
                print(floor)

# Создаем объекты класса House
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

# Вызываем метод go_to у объекта h1
print(f"Переход на этаж {5} в доме '{h1.name}':")
h1.go_to(5)

# Вызываем метод go_to у объекта h2
print(f"\nПопытка перехода на этаж {10} в доме '{h2.name}':")
h2.go_to(10)