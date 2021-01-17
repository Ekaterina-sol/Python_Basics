#Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(self.name, "поехала")

    def stop(self):
        print(self.name, "остановилась")

    def turn(self, direction):
        if direction == "right":
            print(self.name, "поверула направо")
        elif direction == "left":
            print(self.name, "повернула налево")

    def show_speed(self):
        print("Скорость", self.name, self.speed)

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(self.name, "превысила скорость!")
        else:
            print("Скорость", self.name, self.speed)

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Вы превысили скорость!")
        else:
            print("Скорость", self.name, self.speed)

class SportCar(Car):
    def race(self):
        print("Гонка началась!")
        if self.speed > 100:
            print(self.name, "победила!")
        else:
            print(self.name, "проиграла гонку!")

class PoliceCar(Car):
    def pursuit(self):
        print(self.name, "начала погоню!")
        if self.speed > 130:
            print(self.name, "задержала преступника!")
        else:
            print(self.name, "упустила преступника!")

taxi = WorkCar(70, "yellow", "Taxi", False)
taxi.go()
taxi.stop()
taxi.turn("right")
taxi.show_speed()

reno = TownCar(60, "black", "Reno", False)
reno.go()
reno.stop()
reno.turn("left")
reno.show_speed()

ferrary = SportCar(250, "red", "Ferrary", False)
ferrary.go()
ferrary.stop()
ferrary.turn("left")
ferrary.show_speed()
ferrary.race()

police = PoliceCar(150, "black", "Police", True)
police.go()
police.stop()
police.turn("right")
police.show_speed()
police.pursuit()