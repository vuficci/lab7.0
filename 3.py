n = int(input("Введите неотрицательное целое число: "))

factorial = 1

if n >= 0:
    for i in range(1, n + 1):
        factorial *= i

print("Факториал числа", n, ":", factorial)