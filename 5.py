num = int(input("Введите число для таблицы умножения: "))

print("Таблица умножения для", num)
for i in range(1, 11):
    print(num, "x", i, "=", num * i)