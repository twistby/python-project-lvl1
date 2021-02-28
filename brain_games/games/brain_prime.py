"""Brain prime module."""
import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 30


def get_question_and_answer():
    """Return number and is it prime."""
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    right_answer = 'yes' if is_prime(number) else 'no'
    return str(number), right_answer


def is_prime(number):
    """Check is it prime number."""
    if number in {2, 3}:
        return True
    if number % 2 == 0 or number < 2:
        return False
    for step in range(3, int(number ** 0.5) + 1, 2):
        if number % step == 0:
            return False
    return True
