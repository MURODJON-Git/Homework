num = int(input("Введите трехзначное число: "))
hundreds = num // 100
tens = (num // 10) % 10
units = num % 10
new_num = tens * 100 + hundreds * 10 + units
print("Новое число:", new_num)