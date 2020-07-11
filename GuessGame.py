from Live import Game, check_input
from random import randint


class GuessGame(Game):
    secret_number = 0

    def generate_number(self):
        self.secret_number = randint(1, Game.difficulty)
        return self.secret_number

    def get_guess_from_user(self):
        self.guess = input(f'choose a number between 1 to {Game.difficulty}')
        self.guess = check_input(name_of_var=self.guess, range_from=1, range_to=Game.difficulty,
                                 text=f'choose a number between 1 to {Game.difficulty}')
        return self.guess

    def compare_results(self):
        if self.secret_number == self.guess:
            return True
        else:
            return False

    def play(self):
        self.generate_number()
        self.get_guess_from_user()
        if self.compare_results():
            print("You Win")
        else:
            print("You Lose")
