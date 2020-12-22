first_variable = 25;
second_variable = 45;
sum = first_variable + second_variable
print("Первое число: ",first_variable)
print("Второе число: ",second_variable)
print("Сумма чисел: ", sum)
user_name = input("Введите ваше имя: ")
user_city = input("Введите ваше место рождения: ")
user_age = input("Ведите ваш возраст: ")
user_salary = int(input("Ведите вашу зарплату в месяц, руб.: "))
print(f'Добрый день, {user_name}! Вы из {user_city}, Вам {user_age}.')
print(f'Ваша годовая зарплата {12*user_salary} руб.')