"""Brain prime module."""
import random

MAX_RANGE = 30


def get_rules():
    """Return start question."""
    return 'Answer "yes" if given number is prime. Otherwise answer "no"..'


def get_data():
    """Return number and is it prime."""
    number = random.randint(1, MAX_RANGE)
    right_answer = is_prime(number)
    return str(number), right_answer


def is_prime(number):
    """Check is it prime number."""
    if number in {2, 3}:
        return 'yes'
    if number % 2 == 0 or number < 2:
        return 'no'
    for step in range(3, int(number ** 0.5) + 1, 2):
        if number % step == 0:
            return 'no'
    return 'yes'
