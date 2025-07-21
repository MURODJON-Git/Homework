import math 
A = float(input("Write the coordinate A: "))
C = float(input("Write the coordinate C: "))
B = float(input("Write the coordinate B: "))
AC = max(A, C) - min(A, C)
BC = max(B, C) - min(B, C)
print(f"The answer: {AC * BC}")