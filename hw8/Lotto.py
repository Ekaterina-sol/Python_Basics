import math
import random

def new_num(count):
    num_list = []
    while len(num_list) < count:
        new = random.randint(1,90)
        if new not in num_list:
            num_list.append(new)
    return num_list

class Barrel:

    def __init__(self):
        self.number = random.randint(1, 90)

    @property
    def num(self):
        return self.number

    def __str__(self):
        return str(self.number)


class Card:
    rows = 3
    column = 9
    nums_in_row = 5
    data = None
    emptynum = 0
    crossednum = -1

    def __init__(self):
        uniques_count = self.nums_in_row * self.rows
        uniques = new_num(uniques_count)

        self.data = []
        for i in range(0, self.rows):
            tmp = sorted(uniques[self.nums_in_row * i: self.nums_in_row * (i + 1)])
            empty_nums_count = self.column - self.nums_in_row
            for j in range(0, empty_nums_count):
                index = random.randint(0, len(tmp))
                tmp.insert(index, self.emptynum)
            self.data += tmp

    def __str__(self):
        num_list = '--------------------------' + '\n'
        for index, num in enumerate(self.data):
            if num == self.emptynum:
                num_list += '  '
            elif num == self.crossednum:
                num_list += ' -'
            elif num < 10:
                num_list += f' {str(num)}'
            else:
                num_list += str(num)

            if (index + 1) % self.column == 0:
                num_list += '\n'
            else:
                num_list += ' '

        return num_list + '--------------------------'

    def __contains__(self, item):
        return item in self.data

    def cross_num(self, num):
        for index, item in enumerate(self.data):
            if item == num:
                self.data[index] = self.crossednum
                return


    def closed(self) -> bool:
        return set(self.data) == {self.emptynum, self.crossednum}


class Game:
    usercard = None
    compcard = None
    num_barrels = 90
    barrels = []
    def __init__(self):
        self.usercard = Card()
        self.compcard = Card()
        self.barrels = new_num(self.num_barrels)

    def one_play(self) -> int:
        barrel = self.barrels.pop()
        print(f'Новый бочонок: {barrel} (осталось {len(self.barrels)})')
        print(f'----- Ваша карточка ------\n{self.usercard}')
        print(f'-- Карточка компьютера ---\n{self.compcard}')
        useranswer = input('Зачеркнуть цифру? (y/n): ').lower().strip()
        if useranswer == 'y' and not barrel in self.usercard or \
           useranswer != 'y' and barrel in self.usercard:
            return "lose"
        if barrel in self.usercard:
            self.usercard.cross_num(barrel)
            if self.usercard.closed():
                return "win"
        if barrel in self.compcard:
            self.compcard.cross_num(barrel)
            if self.compcard.closed():
                return "lose"

    def play_game(self):
        while True:
            result = game.one_play()
            if result == "win":
                print('Вы победили!')
                break
            elif result == "lose":
                print('Вы проиграли!')
                break

game = Game()
game.play_game()