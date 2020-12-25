my_list = list(input("Введите список: "))
i = 0
for element in range(int(len(my_list)/2)):
    my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
    i +=2
print(my_list)