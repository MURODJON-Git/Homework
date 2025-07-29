num = int(input("Введите число больше 999: "))
thousands_digit = (num // 1000) % 10
print("Цифра в разряде тысяч: ", thousands_digit)