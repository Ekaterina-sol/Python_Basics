
from abc import abstractmethod

class Cloth:

    @property
    @abstractmethod
    def method_1(self):
        return print("Абстрактный метод работает")

    def spending(self, coat_n, suit_n):
        total = coat_n.size / 6.5 + 0.5 + 2 * suit_n.height + 0.3
        return print(f'Общий расход ткани: {total:.2f}')

class Coat(Cloth):
    def __init__(self, size):
        self.size = size

    @property
    def cloth_spend(self):
        coat_cloth = (self.size/6.5) + 0.5
        return f'Расход ткани на пальто: {coat_cloth:.2f}'

    def abstract(self):
        return 'Абстрактный метод работает для пальто'

class Suit(Cloth):
    def __init__(self, height):
        self.height = height

    @property
    def cloth_spend(self):
        suit_cloth = 2 * self.height + 0.3
        return f'Расход ткани на костюм: {suit_cloth:.2f}'

    def abstract(self):
        return 'Абстрактный метод работает для пальто'

coat = Coat(500)
print(coat.cloth_spend)
suit = Suit(160)
print(suit.cloth_spend)
coat.spending(coat, suit)
coat.method_1
suit.method_1