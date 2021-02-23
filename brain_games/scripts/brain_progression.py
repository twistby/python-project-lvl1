"""Brain progression script."""
from brain_games import game_engine
from brain_games.games import brain_progression_game


def main():
    """Run script."""
    game_engine.start(brain_progression_game)


if __name__ == '__main__':
    main()
