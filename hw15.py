a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))
unique_numbers = {a, b, c}
if len(unique_numbers) < 3:
    print("Да ✅ — есть хотя бы одна пара совпадающих чисел.")
else:
    print("Нет ❌ — все три числа разные.")