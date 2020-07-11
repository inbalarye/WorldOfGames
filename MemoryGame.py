from Live import Game, check_input
import random


class MemoryGame(Game):
    def generate_sequence(self):
        self.randlist = random.sample(range(1, 101), Game.difficulty)
        print(self.randlist)
        return self.randlist

    def get_list_from_user(self):
        self.userlist = []
        for number in range(Game.difficulty):
            number = input(f'please enter the numbers that you remember in size {self.difficulty} ')
            number = check_input(name_of_var=number, range_from=1, range_to=101, text=f'please enter the numbers that '
                                                                                      f'you remember in size '
                                                                                      f'{self.difficulty} ')
            self.userlist.append(number)
        return self.userlist

    def is_list_equal(self):
        if self.randlist == self.userlist:
            return True
        else:
            return False

    def play(self):
        self.generate_sequence()
        self.get_list_from_user()
        if self.is_list_equal():
            print('You Win')
        else:
            print('You Lose')


