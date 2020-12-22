import math
user_incomes = int(input("Введите текущую выручку: "))
user_expenses = int(input("Введите текущие издержки: "))

if user_incomes > user_expenses:
    margin = user_incomes - user_expenses
    user_profitability = margin*100 / user_incomes
    user_profitability = float('{:.2f}'.format(user_profitability))
    print("Ваша фирма работает с прибылью. Прибыль составялет:", margin)
    print("Рентабельность выручки составялет:", user_profitability, "%")
    staff_number = int(input("Введите количество работников: "))
    print("Прибыль фирмы в расчете на одного сотрудника составялет:", margin / staff_number)
elif user_incomes == user_expenses:
    print("Ваша фирма работает в ноль")
else:
    loss = user_expenses - user_incomes
    print("Ваша фирма работает в убыток. Убыток составялет:", loss)