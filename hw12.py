A = int(input("Введите A: "))
B = int(input("Введите B: "))
C = int(input("Введите C: "))
count = (A > 0) + (B > 0) + (C > 0)
if count == 2:
    print("Ровно два числа положительные.")
else:
    print("Не ровно два числа положительные.")