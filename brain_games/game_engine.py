"""Brain games body."""
from brain_games import cli

ANSWERS_TO_WIN = 3


def start(game):
    """Start the game."""
    cli.welcome_user()
    user_name = cli.get_user_name()
    stop_game(user_name, run(game))


def run(game):
    """Run game. Return True if won, False if lose."""
    print(game.get_rules())
    for _ in range(ANSWERS_TO_WIN):
        question, right_answer = game.get_data()
        print('Question: {q}'.format(q=question))
        answer = cli.get_answer('Your answer: ')
        if answer == right_answer:
            print('Correct!')
        else:
            show_answers(answer, right_answer)
            return False
    return True


def stop_game(user_name, user_won):
    """Stop and show game result."""
    if user_won:
        message = 'Congratulations,'
    else:
        message = "Let's try again,"
    print(message + ' {user_name}!'.format(user_name=user_name))


def show_answers(answer, right_answer):
    """Print user answer and right answer."""
    msg1 = "'{a}' is wrong answer ;(. Correct answer".format(a=answer)
    msg2 = " was '{ra}'.".format(ra=right_answer)
    print(msg1 + msg2)
