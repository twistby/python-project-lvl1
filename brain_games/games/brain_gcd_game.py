"""Brain gcd module."""
import random

from brain_games import constants


def get_main_question():
    """Return start question."""
    return 'Find the greatest common divisor of given numbers.'


def get_data():
    """Found GCD of two numbers."""
    f_number = random.randint(1, constants.GAME_GCD_FIRST_RANGE)
    s_number = random.randint(1, constants.GAME_GCD_SECOND_RANGE)
    question = '{f} {s}'.format(f=f_number, s=s_number)
    right_answer = get_gcd(f_number, s_number)
    return question, str(right_answer)


def get_gcd(f_number, s_number):
    """Found GCD of two numbers."""
    while f_number != 0 and s_number != 0:
        if f_number > s_number:
            f_number %= s_number
        else:
            s_number %= f_number
    return f_number + s_number
