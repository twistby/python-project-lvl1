"""Brain calc module."""
import operator
import random

DESCRIPTION = 'What is the result of the expression?'
MIN_FIRST_NUMBER = 1
MAX_FIRST_NUMBER = 30
MIN_SECOND_NUMBER = 1
MAX_SECOND_NUMBER = 10


def get_question_and_answer():
    """Generate two numbers and return operation result."""
    calculation_functions = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }
    first_number = random.randint(MIN_FIRST_NUMBER, MAX_FIRST_NUMBER)
    second_number = random.randint(MIN_SECOND_NUMBER, MAX_SECOND_NUMBER)
    operation = random.choice(list(calculation_functions.keys()))
    right_answer = calculation_functions.get(operation)(
        first_number,
        second_number,
    )
    question = '{f} {o} {s}'.format(
        f=first_number,
        o=operation,
        s=second_number)
    return question, str(right_answer)
