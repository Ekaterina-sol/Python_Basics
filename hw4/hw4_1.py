import sys

working_time, rate, bonus = sys.argv[1:]
working_time = float(working_time)
rate = float(rate)
bonus = float(bonus)
salary = working_time * rate + bonus
print(f'заработная плата сотрудника  {salary}')
