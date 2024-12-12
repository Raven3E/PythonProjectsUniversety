numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

for num in numbers:
    if num == 1:
        continue
    is_prime = True

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
    else:
        not_primes.append(num)
print("Primes:", primes)
print("Not_Primes:", not_primes)



def get_matrix(n, m, value):
    """
    Создает матрицу размерами n x m, заполненную значением value.

    :param n: Количество строк матрицы
    :param m: Количество столбцов матрицы
    :param value: Значение для заполнения матрицы
    :return: Матрица в виде вложенного списка
    """
    # Если размеры матрицы некорректны (0 или отрицательные значения), возвращаем пустой список
    if n <= 0 or m <= 0:
        return []

    # Создаем пустой список для хранения всей матрицы
    matrix = []

    # Внешний цикл для строк матрицы
    for _ in range(n):
        # Создаем строку матрицы
        row = []

        # Внутренний цикл для столбцов матрицы
        for _ in range(m):
            # Добавляем значение в строку
            row.append(value)

        # Добавляем готовую строку в матрицу
        matrix.append(row)

    # Возвращаем итоговую матрицу
    return matrix

# Примеры использования
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

# Вывод результатов
print(result1)
print(result2)
print(result3)
