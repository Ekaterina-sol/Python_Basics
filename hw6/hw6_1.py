
import time

class TrafficLight:
    def __init__(self):
        self.__color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        while i != 3:
            print(self.__color[0])
            time.sleep(7)
            print(self.__color[1])
            time.sleep(2)
            print(self.__color[2])
            time.sleep(5)
            i += 1
        print("Ремонтные работы")

first_traffic = TrafficLight()
first_traffic.running()