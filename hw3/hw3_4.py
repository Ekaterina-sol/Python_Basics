import math

number_1 = float(input("Введите положительное число: "))
number_2 = int(input("Введите целое отрицательное число: "))

def my_func(number_1, number_2):
    result = number_1 ** number_2
    return result

def my_func2(number_1, number_2):
    result = number_1
    if number_2 == - 1:
       return 1/result
    else:
        for i in range(1, abs(number_2)):
            result = result * number_1
            i += 1
        return 1/result
print("Результат возведения в степень способом 1: ", my_func(number_1, number_2))
print("Результат возведения в степень способом 2: ", my_func2(number_1, number_2))