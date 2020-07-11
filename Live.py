def check_input(name_of_var, range_from, range_to, text):
    if name_of_var.isdigit():
        name_of_var = int(name_of_var)
    while name_of_var not in range(range_from, range_to + 1):
        print(text)
        name_of_var = input()
        while not name_of_var.isdigit():
            print(text)
            name_of_var = input()
        name_of_var = int(name_of_var)
    return name_of_var


class Game(object):
    difficulty = 0
    game = 0

    def lode_game(self):
        Game.game = input('Please choose a game to play:\n '
                          '1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it '
                          'back .\n2. Guess Game - guess a number and see if you chose like the computer. \n'
                          '3. Currency Roulette - try and guess the value of a random amount od USD in ILS.')
        Game.game = check_input(name_of_var=Game.game, range_from=1, range_to=3,
                                text='please choose a number between 1 to 3')
        Game.difficulty = input('Please choose game difficulty from 1 to 5:')
        Game.difficulty = check_input(name_of_var=Game.difficulty, range_from=1, range_to=5,
                                      text='Please choose game difficulty from 1 to 5:')

    def welcome(self, name):
        print(f'Hello {name} and welcome to the World of Games(WoG)\n Here you can find many cool games to play.')
