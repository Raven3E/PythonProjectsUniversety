def generate_password(n):
    result = ""
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if (i + j) % n == 0:
                result += str(i) + str(j)
    return result

n = int(input("Введите число от 3 до 20: "))
if 3 <= n <= 20:
    password = generate_password(n)
    print(f"Сгенерированный пароль для {n}: {password}")
else:
    print("Число должно быть в диапазоне от 3 до 20.")
