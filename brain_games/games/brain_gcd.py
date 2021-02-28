"""Brain gcd module."""
import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'
MIN_FIRST_NUMBER = 1
MAX_FIRST_NUMBER = 1000
MIN_SECOND_NUMBER = 1
MAX_SECOND_NUMBER = 100


def get_question_and_answer():
    """Return GCD of two numbers."""
    first_number = random.randint(MIN_FIRST_NUMBER, MAX_FIRST_NUMBER)
    second_number = random.randint(MIN_SECOND_NUMBER, MAX_SECOND_NUMBER)
    question = '{f} {s}'.format(f=first_number, s=second_number)
    right_answer = get_gcd(first_number, second_number)
    return question, str(right_answer)


def get_gcd(f_number, s_number):
    """Found GCD of two numbers."""
    while f_number != 0 and s_number != 0:
        if f_number > s_number:
            f_number %= s_number
        else:
            s_number %= f_number
    return f_number + s_number
