number = int(input("Введите целое положительное число: "))
if 10 <= number <= 99 and number % 2 == 0:
    print("✅ Число является чётным двузначным.")
else:
    print("❌ Число не является чётным либо двузначным.")