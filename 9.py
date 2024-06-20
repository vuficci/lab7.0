n = int(input("Введите натуральное число: "))

if n > 0:
    for i in range(n, 0, -1):
        print(i)
else:
    print("Число должно быть натуральным.")