"""Brain even script."""
from brain_games import game_body
from brain_games.games import brain_even_game


def main():
    """Run script."""
    game_body.start_game(brain_even_game)


if __name__ == '__main__':
    main()
