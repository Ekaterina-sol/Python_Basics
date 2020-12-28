import math

def total_sum ():
    user_sum = 0
    while True:
        try:
            user_string = input("Чтобы завершить работу программы ведите q вместо числа. Введите строку чисел через пробел: ")
            user_list = user_string.split(' ')
            if user_string.count("q") > 0:
                user_list.remove("q")
                user_number = [int(number) for number in user_list]
                user_sum = user_sum + sum(user_number)
                break
            else:
                user_number = [int(number) for number in user_list]
                user_sum = user_sum + sum(user_number)
                print("Промежуточная сумма всех чисел равна: ", user_sum)
        except ValueError:
            print("Вы ввели не цифру или дополнительный пробел. Введите строку чисел заново")
    print("Итоговая сумма всех чисел равна: ", user_sum)

total_sum()