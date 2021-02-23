"""Brain even script."""
from brain_games import game_engine
from brain_games.games import brain_even_game


def main():
    """Run script."""
    game_engine.start(brain_even_game)


if __name__ == '__main__':
    main()
