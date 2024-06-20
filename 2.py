num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))

maximum = num1

if num2 > maximum:
    maximum = num2
if num3 > maximum:
    maximum = num3

print("Максимальное число:", maximum)