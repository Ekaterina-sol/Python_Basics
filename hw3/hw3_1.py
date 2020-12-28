def digits_division():
    try:
        digit_1 = int(input("Введите делимое число: "))
        digit_2 = int(input("Введите делитель: "))
        result = digit_1 / digit_2
    except ZeroDivisionError:
        print('Делить на ноль нельзя')
    except ValueError:
        print('Вы ввели не число')
    else:
        return result

print(digits_division())

