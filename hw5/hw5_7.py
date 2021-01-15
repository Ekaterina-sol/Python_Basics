import json
with open('text7.txt', 'r', encoding='utf-8') as f:
    company_profit = {}
    average = {}
    names = []
    profits = []
    aver_profit = 0
    i = 0
    for line in f:
        com_profit = 0
        name, own, revenue, expenses = line.split()
        com_profit = int(revenue) - int(expenses)
        names.append(name)
        profits.append(com_profit)
        company_profit = dict(zip(names, profits))
        print(f"Прибыль компании {name}: ", com_profit)
        if com_profit >= 0:
            total_profit = com_profit + com_profit
            i = i + 1
        aver_profit = total_profit / i
        average = {"Средняя прибыль компаний": aver_profit}
print(average)
print(f"Прибыли и убытки компаний: \n", company_profit)
total = [company_profit, average]
print(total)
f.close()
with open('text7_new.json', 'w', encoding='utf-8') as f_js:
    json.dump(total, f_js)
f_js.close()