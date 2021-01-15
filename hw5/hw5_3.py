import math
f = open('text3.txt', encoding='utf-8')
user_list = f.read().split('\n')
print(user_list)
low_salary = []
salary = []
for user in user_list:
        user = user.split()
        if int(user[1]) < 20000:
           low_salary.append(user[0])
        salary.append(user[1])
print(f'Сотрудники с окладом меньше 20 тыс.:  {low_salary}')
print (f'Средняя величина дохода:  {sum(map(int, salary)) / len(salary)}')
f.close()
