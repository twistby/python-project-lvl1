"""Brain calc script."""
from brain_games import game_engine
from brain_games.games import brain_calc_game


def main():
    """Start of script."""
    game_engine.start(brain_calc_game)


if __name__ == '__main__':
    main()
