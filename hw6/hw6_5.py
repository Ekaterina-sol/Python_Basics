
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки...")

class Pen(Stationery):
    def draw(self):
        print("Отрисовка ручкой")

class Pencil(Stationery):
    def draw(self):
        print("Отрисовка карандашем")

class Handle(Stationery):
    def draw(self):
        print("Отрисовка маркером")

stat = Stationery("stat")
stat.draw()

pen = Pen("pen")
pen.draw()

pencil = Pencil("pencil")
pencil.draw()

handle = Handle("handle")
handle.draw()