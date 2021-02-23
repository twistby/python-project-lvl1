"""Brain gcd module."""
import random
from math import gcd

MAX_FIRST_RANGE = 1000
MAX_SECOND_RANGE = 100


def get_rules():
    """Return start question."""
    return 'Find the greatest common divisor of given numbers.'


def get_data():
    """Return GCD of two numbers."""
    first_number = random.randint(1, MAX_FIRST_RANGE)
    second_number = random.randint(1, MAX_SECOND_RANGE)
    question = '{f} {s}'.format(f=first_number, s=second_number)
    right_answer = gcd(first_number, second_number)
    return question, str(right_answer)
