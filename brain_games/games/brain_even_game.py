"""Brain even module."""
import random

MAX_RANGE = 100


def get_rules():
    """Return start question."""
    return 'Answer "yes" if the number is even, otherwise answer "no".'


def get_data():
    """Return number and is it even."""
    number = random.randint(1, MAX_RANGE)
    right_answer = 'yes' if number % 2 == 0 else 'no'
    return str(number), str(right_answer)
