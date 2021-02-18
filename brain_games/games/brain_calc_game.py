"""Brain calc scriptmodule."""
import random

from brain_games import cli, constants


def game():
    """Game circle. Return True if win, False if lose."""
    cli.pr_str('What is the result of the expression?')
    for _ in range(constants.NUMBER_OF_TRY):
        f_number = random.randint(1, constants.GAME_CALC_FIRST_RANGE)
        s_number = random.randint(1, constants.GAME_CALC_SECOND_RANGE)
        right_answer, op = get_operation(f_number, s_number)
        cli.pr_str('Question: {f} {o} {s}'.format(f=f_number, o=op, s=s_number))
        answer = cli.ask('Your answer: ')
        if answer == str(right_answer):
            cli.pr_str('Correct!')
        else:
            cli.pr_wrong_answ(answer, right_answer)
            return False
    return True


def get_operation(f_number, s_number):
    """Chose operation and found right answer."""
    operation = random.randint(1, 3)
    if operation == 1:
        right_answer = f_number + s_number
        op = '+'
    elif operation == 2:
        right_answer = f_number - s_number
        op = '-'
    else:
        right_answer = f_number * s_number
        op = '*'
    return right_answer, op


def start_game():
    """Start the game."""
    cli.welcome_user()
    user_name = cli.ask_user_name()
    cli.end_game(user_name, game())
