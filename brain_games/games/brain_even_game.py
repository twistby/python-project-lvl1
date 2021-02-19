"""Brain even module."""
import random

from brain_games import constants


def get_main_question():
    """Return start question."""
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def get_data():
    """Generate number and even."""
    current_number = random.randint(1, constants.GAME_EVEN_RANGE)
    right_answer = 'yes' if current_number % 2 == 0 else 'no'
    question = '{n}'.format(n=current_number)
    return question, str(right_answer)
