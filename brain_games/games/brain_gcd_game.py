"""Brain gcd module."""
import random

from brain_games import cli, constants


def game():
    """Game circle. Return True if win, False if lose."""
    cli.pr_str('Find the greatest common divisor of given numbers.')
    for _ in range(constants.NUMBER_OF_TRY):
        f_number = random.randint(1, constants.GAME_GCD_FIRST_RANGE)
        s_number = random.randint(1, constants.GAME_GCD_SECOND_RANGE)
        right_answer = get_gcd(f_number, s_number)
        cli.pr_str('Question: {f} {s}'.format(f=f_number, s=s_number))
        answer = cli.ask('Your answer: ')
        if answer == str(right_answer):
            cli.pr_str('Correct!')
        else:
            cli.pr_wrong_answ(answer, right_answer)
            return False
    return True


def get_gcd(f_number, s_number):
    """Found GCD of two numbers."""
    while f_number != 0 and s_number != 0:
        if f_number > s_number:
            f_number %= s_number
        else:
            s_number %= f_number
    return f_number + s_number


def start_game():
    """Start the game."""
    cli.welcome_user()
    user_name = cli.ask_user_name()
    cli.end_game(user_name, game())
