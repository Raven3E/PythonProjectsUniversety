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

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

# Создаем объекты класса House
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# Пример использования метода __str__
print(h1)  # Вывод: Название: ЖК Эльбрус, кол-во этажей: 10
print(h2)  # Вывод: Название: ЖК Акация, кол-во этажей: 20

# Пример использования метода __len__
print(len(h1))  # Вывод: 10
print(len(h2))  # Вывод: 20