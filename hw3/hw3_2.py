def user_data(**kwargs):
    return list(kwargs.items())

print(user_data(name = input('Имя: '), surname = input('Фамилия: '), year = input('Год рождения: '), city = input('Город проживания: '), email = input('email: '), phone = input('Телефон: ')))