with open('text5.txt', 'w', encoding='utf-8') as f:
    user_string = input("Введите набор чисел через пробел: ")
    f.writelines(user_string)
    user_numbers = user_string.split(' ')
    print(sum(map(int, user_numbers)))
f.close()