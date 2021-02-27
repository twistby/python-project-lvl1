"""Brain even script."""
from brain_games import game_engine
from brain_games.games import brain_even


def main():
    """Run script."""
    game_engine.play(brain_even)


if __name__ == '__main__':
    main()
