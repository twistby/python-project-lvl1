"""Brain prime script."""
from brain_games import game_engine
from brain_games.games import brain_pime_game


def main():
    """Run script."""
    game_engine.start(brain_pime_game)


if __name__ == '__main__':
    main()
