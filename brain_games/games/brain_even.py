"""Brain even module."""
import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def get_question_and_answer():
    """Return number and is it even."""
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    right_answer = 'yes' if number % 2 == 0 else 'no'
    return str(number), right_answer
