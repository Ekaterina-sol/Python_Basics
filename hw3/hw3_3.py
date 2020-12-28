import math
number_1 = int(input("Введите первое число: "))
number_2 = int(input("Введите второе число: "))
number_3 = int(input("Введите третье число: "))

def my_func(number_1, number_2, number_3):
    result = number_1 + number_2 + number_3 - min(number_1,number_2,number_3)
    return result

print("Сумма двух наибольших чисел равна: ", my_func(number_1, number_2, number_3))

