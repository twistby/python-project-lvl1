"""Brain even module."""
import random

from brain_games import cli, constants


def game():
    """Game circle. Return True if win, False if lose."""
    cli.pr_str('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(constants.NUMBER_OF_TRY):
        current_number = random.randint(1, constants.GAME_EVEN_RANGE)
        right_answer = 'yes' if current_number % 2 == 0 else 'no'
        cli.pr_str('Question: {cn}'.format(cn=current_number))
        answer = cli.ask('Your answer: ')
        if answer == right_answer:
            print('Correct!')
        else:
            cli.pr_wrong_answ(answer, right_answer)
            return False
    return True


def start_game():
    """Start the game."""
    cli.welcome_user()
    user_name = cli.ask_user_name()
    cli.end_game(user_name, game())
