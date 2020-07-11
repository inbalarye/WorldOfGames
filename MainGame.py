from Live import Game, check_input
from GuessGame import GuessGame
from MemoryGame import MemoryGame
from CurrencyRouletteGame import CurrencyGame


def choose_game(game):
    if game == 1:
        MemoryGame().play()
    elif game == 2:
        GuessGame().play()
    else:
        CurrencyGame().play()


Game().lode_game()
choose_game(Game.game)

