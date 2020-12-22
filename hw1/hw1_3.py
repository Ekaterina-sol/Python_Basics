user_number = int(input("Введите число от 1 до 9: "))
tens = user_number*10 + user_number
hundreds = user_number*100 + tens
sum = user_number + tens + hundreds
print("Посчитаем", user_number, "+", tens, "+", hundreds, ". Сумма равна: ", sum)