"""Brain even script."""
from brain_games import game_engine
from brain_games.games import brain_gcd


def main():
    """Run script."""
    game_engine.play(brain_gcd)


if __name__ == '__main__':
    main()
