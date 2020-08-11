import random
import time
from typing import List

from abstract import Observer, Observed


class Player(Observer):
    def __init__(self, name: str):
        self.name = name
        self.lottery_ticket: List[int] = random.sample(range(1, 100), 5)

    def handle_event(self, lottery_number: int):
        if lottery_number in self.lottery_ticket:
            self.lottery_ticket.remove(lottery_number)

        if not self.lottery_ticket:
            print(f'{self.name.upper()} BINGO!!!')
            quit()

    def __str__(self):
        return self.name


class Lottery(Observed):
    def __init__(self):
        print('Welcome to the bingo game')
        self._numbers_streak: List[int] = list()
        self.players: List[Player] = list()

    def generate_number(self):
        generated_number: int = random.randint(1, 99)
        self._numbers_streak.append(generated_number)
        self.notify_observers(generated_number)
        time.sleep(0.1)

    def add_observer(self, p: Player):
        self.players.append(p)

    def remove_observer(self, p: Player):
        self.players.remove(p)

    def notify_observers(self, lottery_number: int):
        print(f'We got number: {lottery_number}')

        for i in self.players:
            i.handle_event(lottery_number)


if __name__ == '__main__':
    # Client Code
    p1 = Player('Aslan')
    p2 = Player('Ersain')
    p3 = Player('Akhmet')
    p4 = Player('Alisher')
    p5 = Player('Dima')

    my_lottery_players: List[Player] = [p1, p2, p3, p4, p5]

    my_lottery = Lottery()
    for i in my_lottery_players:
        my_lottery.add_observer(i)
        print(f'New player {i} has joined the game.')

    while True:
        my_lottery.generate_number()
