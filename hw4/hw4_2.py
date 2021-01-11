import math
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123,55]
new_list = [number for number in my_list if number > my_list[my_list.index(number)-1]]
new_list.pop(0)
print(new_list)