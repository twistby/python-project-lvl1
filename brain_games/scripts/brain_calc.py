"""Brain calc script."""
from brain_games import game_engine
from brain_games.games import brain_calc


def main():
    """Start of script."""
    game_engine.play(brain_calc)


if __name__ == '__main__':
    main()
