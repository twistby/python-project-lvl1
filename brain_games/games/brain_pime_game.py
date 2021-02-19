"""Brain prime module."""
import random

from brain_games import constants


def get_main_question():
    """Return start question."""
    return 'Answer "yes" if given number is prime. Otherwise answer "no"..'


def get_data():
    """Generate number."""
    current_number = random.randint(1, constants.GAME_PRIME_RANGE)
    right_answer = is_prime(current_number)
    question = '{n}'.format(n=current_number)
    return question, right_answer


def is_prime(num):
    """Is number prime."""
    if num > 1:
        for _ in range(2, num):
            if (num % _) == 0:
                return 'no'
        return 'yes'
    return 'no'
