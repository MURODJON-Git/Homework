a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
d = int(input("Введите четвертое число: "))
numbers = [a, b, c, d]
for i in range(4):
    if numbers.count(numbers[i]) == 1:
        print("Порядковый номер отличающегося числа:", i + 1)
        break