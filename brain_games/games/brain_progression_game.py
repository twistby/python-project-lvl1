"""Brain progression module."""
import random

MAX_START_NUMBER = 15
MAX_LEGHT = 15
MAX_STEP = 10


def get_rules():
    """Return start question."""
    return 'What number is missing in the progression?'


def get_data():
    """Make progression and right answer."""
    start = random.randint(1, MAX_START_NUMBER)
    leght = random.randint(5, MAX_LEGHT)
    step = random.randint(1, MAX_STEP)
    lost_position = random.randint(0, leght - 1)
    return get_progression_and_answer(start, leght, step, lost_position)


def get_progression_and_answer(start, leght, step, lost_position):
    """Generate question and right answer."""
    progression = []
    for position in range(leght):
        if position == lost_position:
            progression.append('..')
            right_answer = str(start)
        else:
            progression.append(start)
        start += step
    question = ' '.join([str(elem) for elem in progression])
    return question, right_answer
