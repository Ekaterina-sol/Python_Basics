month = int(input("Введите номер месяца: "))

season_list = ["зима", "весна", "лето", "осень"]

if month == 1 or month == 2 or month == 12:
    print("Время года: ", season_list[0])
elif month == 3 or month == 4 or month == 5:
    print("Время года: ", season_list[1])
elif month == 6 or month == 7 or month == 8:
    print("Время года: ", season_list[2])
elif month == 9 or month == 10 or month == 11:
    print("Время года: ", season_list[3])
else:
    print("Вы ввели неправильное число")

year = {
    'зима': {1, 2, 12},
    'весна': {3, 4, 5},
    'лето': {6, 7, 8},
    'осень': {9, 10, 11},
}

for key in year.keys():
    if month in year[key]:
        print("Время года: ", key)
    elif month < 1 or month > 12:
        print("Вы ввели неправильное число")
        break
