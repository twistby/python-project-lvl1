"""Brain progression module."""
import random

RULES = 'What number is missing in the progression?'
MIN_START_NUMBER = 1
MAX_START_NUMBER = 15
MIN_PROGRESSION_LENGTH = 5
MAX_PROGRESSION_LENGTH = 15
MIN_PROGRESSION_STEP = 1
MAX_PROGRESSION_STEP = 10


def get_question_and_answer():
    """Make progression and right answer."""
    start = random.randint(MIN_START_NUMBER, MAX_START_NUMBER)
    length = random.randint(MIN_PROGRESSION_LENGTH, MAX_PROGRESSION_LENGTH)
    step = random.randint(MIN_PROGRESSION_STEP, MAX_PROGRESSION_STEP)
    hidden_position = random.randint(0, length - 1)
    return get_progression_and_answer(start, length, step, hidden_position)


def get_progression_and_answer(start, length, step, hidden_position):
    """Generate question and right answer."""
    progression = []
    current_number = start
    for position in range(length):
        if position == hidden_position:
            progression.append('..')
            right_answer = str(current_number)
        else:
            progression.append(current_number)
        current_number += step
    question = ' '.join([str(elem) for elem in progression])
    return question, right_answer
