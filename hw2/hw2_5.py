my_list = [7, 5, 3, 3, 2]
print("Текущий рейтинг: ", my_list)
user_number = int(input("Введите новый элемент рейтинга: "))
my_list = sorted(my_list)
quantity = my_list.count(user_number)

if quantity > 0:
    position = my_list.index(user_number)
    add_list = my_list.insert(position, user_number)
    new_list = my_list[::-1]
    print(new_list)
else:
    add_list = my_list.append(user_number)
    sort_list = my_list.sort(reverse = True)
    print(my_list)

