"""Brain calc module."""
import random

MAX_FIRST_RANGE = 30
MAX_SECOND_RANGE = 10


def get_rules():
    """Return start question."""
    return 'What is the result of the expression?'


def get_data():
    """Generate two numbers and operation result."""
    first_number = random.randint(1, MAX_FIRST_RANGE)
    second_number = random.randint(1, MAX_SECOND_RANGE)
    oper = random.choice(['+', '-', '*'])
    if oper == '+':
        right_answer = first_number + second_number
    elif oper == '-':
        right_answer = first_number - second_number
    else:
        right_answer = first_number * second_number
    question = '{f} {o} {s}'.format(f=first_number, o=oper, s=second_number)
    return question, str(right_answer)
