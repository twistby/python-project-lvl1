"""Brain progression module."""
import random

from brain_games import constants


def get_main_question():
    """Return start question."""
    return 'What number is missing in the progression?'


def get_data():
    """Make progression and right answer."""
    pr_first_number = random.randint(1, constants.GAME_PROGRESSION_MAX_START_N)
    pr_leght = random.randint(5, constants.GAME_PROGRESSION_MAX_LEGHT)
    pr_step = random.randint(1, constants.GAME_PROGRESSION_MAX_STEP)
    lost_number_pos = random.randint(0, pr_leght - 1)
    pr = []
    right_answer = ''
    for _ in range(pr_leght):
        if _ == lost_number_pos:
            pr.append('..')
            right_answer = str(pr_first_number)
        else:
            pr.append(pr_first_number)
        pr_first_number += pr_step
    question = ' '.join([str(elem) for elem in pr])
    return question, right_answer
