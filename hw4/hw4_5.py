from functools import reduce

my_list = [number for number in range(99, 1001) if number % 2 == 0]

print(reduce(lambda x, y: x*y, my_list))
