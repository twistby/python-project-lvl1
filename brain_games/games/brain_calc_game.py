"""Brain calc module."""
import random

from brain_games import constants


def get_main_question():
    """Return start question."""
    return 'What is the result of the expression?'


def get_data():
    """Generate two numbers and operation result."""
    f_number = random.randint(1, constants.GAME_CALC_FIRST_RANGE)
    s_number = random.randint(1, constants.GAME_CALC_SECOND_RANGE)
    right_answer, op = get_operation(f_number, s_number)
    question = '{f} {o} {s}'.format(f=f_number, o=op, s=s_number)
    return question, str(right_answer)


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
