from Live import Game, check_input
from forex_python.converter import CurrencyRates
import random


class CurrencyGame(Game):

    def get_money_interval(self):
        self.number = random.randint(1, 100)
        currency = CurrencyRates().get_rates('USD')['ILS'] * self.number
        self.money_interval_low = currency - (5 - Game.difficulty)
        self.money_interval_top = currency + (5 - Game.difficulty)
        return self.money_interval_low, self.money_interval_top

    def get_guess_from_user(self):
        self.guess = input(f'Please guess amount of USD of {self.number}')
        self.guess = float(self.guess)
        return self.guess

    def play(self):
        self.get_money_interval()
        self.get_guess_from_user()
        if self.money_interval_low <= self.guess <= self.money_interval_top:
            print('You Win')
        else:
            print('You Lose')
