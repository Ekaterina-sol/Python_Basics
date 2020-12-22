import math
user_number = int(input("Введите время в секундах: "))
hour = math.floor(user_number / 3600)
min = math.floor((user_number % 3600) / 60)
sec =  (user_number % 3600) % 60
print("Введенное время {:02}:{:02}:{:02}".format(hour,min,sec))