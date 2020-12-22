import math

user_number = int(input("Введите ваш результат в км в первый день пробежки: "))
wish_number = int(input("Введите ваш желаемый результат в км за день: "))

day = 0

while user_number < wish_number:
    day += 1
    user_number = user_number * 1.1
    result = float('{:.2f}'.format(user_number))
    print(day,"-й день:", result, "км")

print(f'на {day} день спортсмен достиг результата — не менее {wish_number} км')
