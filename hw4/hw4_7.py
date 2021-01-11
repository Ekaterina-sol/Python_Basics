import math

n = int(input("Введите число n: "))

def fact(n):
    for number in range (1, n+1):
        yield number

for el in fact(n):
    print(f"{el}! = {math.factorial(el)}")
