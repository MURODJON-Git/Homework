A = float(input("Введите A: "))
B = float(input("Введите B: "))
C = float(input("Введите C: "))
if A < B < C:
    A *= 2
    B *= 2
    C *= 2
else:
    A = -A
    B = -B
    C = -C
print("Новые значения:")
print("A =", A)
print("B =", B)
print("C =", C)