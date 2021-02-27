"""Brain prime script."""
from brain_games import game_engine
from brain_games.games import brain_prime


def main():
    """Run script."""
    game_engine.play(brain_prime)


if __name__ == '__main__':
    main()
