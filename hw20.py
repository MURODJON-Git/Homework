A = float(input("Введите координату точки A: "))
B = float(input("Введите координату точки B: "))
C = float(input("Введите координату точки C: "))
dist_B = abs(B - A)
dist_C = abs(C - A)
if dist_B < dist_C:
    print("Ближе к A находится точка B")
    print("Расстояние от A до B:", dist_B)
elif dist_C < dist_B:
    print("Ближе к A находится точка C")
    print("Расстояние от A до C:", dist_C)
else:
    print("Точки B и C находятся на одинаковом расстоянии от A")
    print("Расстояние:", dist_B)