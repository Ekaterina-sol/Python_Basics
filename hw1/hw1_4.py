import math
user_number = int(input("Введите целое положительное число: "))
max_number = -1
last_number = user_number % 10

while user_number > 0:
    user_number = user_number // 10
    if user_number % 10 > max_number:
        max_number = user_number % 10
    elif last_number > max_number:
        max_number = last_number
print("Самая большая цифра в вашем числе:",max_number)