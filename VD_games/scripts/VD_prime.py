from VD_games.engine import run_game
from VD_games.games.vd_prime import get_game


def main():
    description, game = get_game()
    run_game(description, game)
