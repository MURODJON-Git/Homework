import math 
A = float(input("Write the coordinate A: "))
B = float(input("Write the coordinate B: "))
C = float(input("Write the coordinate C: "))
AC = abs(A - C)
BC = abs(B - C)
sum_segments = AC + BC 
print(f"The length of AC: {AC}")
print(f"The length of BC: {BC}")
print(f"Sum of AC AND BC: {sum_segments}")