# import math
# def rectangle_properties(x1, x2, y1, y2) :
#     width = abs(x2 - x1)
#     height = abs(y1 - y2)
#     perimeter = 2 * (width + height)
#     area = width * height
#     return perimeter, area 
# x1, y1 = 1, 2
# x2, y2 = 3, 4
# perim, square = rectangle_properties(x1, x2, y1, y2)
# print(f"Perimeter: {perim}")
# print(f"Area: {square}")

x1, y1 = 1, 2
x2, y2 = 3, 4
width = abs(x2 - x1)
height = abs(y1 - y2)
perimeter = 2 * (width + height)
area = width * height
print(f"Perimeter: {perimeter}")
print(f"Area: {area}")

