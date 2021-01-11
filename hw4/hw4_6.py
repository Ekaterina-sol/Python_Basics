from itertools import count, cycle

for el in count(3):
    if el > 10:
        break
    else:
        print(el)

с = 0
for el in cycle("NICK"):
    if с > 10:
        break
    print(el)
    с += 1



