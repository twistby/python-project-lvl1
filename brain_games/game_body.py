"""Brain games body."""
from brain_games import cli, constants


def start_game(game):
    """Start the game."""
    cli.welcome_user()
    user_name = cli.ask_user_name()
    cli.end_game(user_name, circle(game))


def circle(game):
    """Game circle. Return True if win, False if lose."""
    cli.pr_str(game.get_main_question())
    for _ in range(constants.NUMBER_OF_TRY):
        question, right_answer = game.get_data()
        cli.pr_str('Question: {question}'.format(question=question))
        answer = cli.ask('Your answer: ')
        if answer == right_answer:
            cli.pr_str('Correct!')
        else:
            cli.pr_wrong_answ(answer, right_answer)
            return False
    return True
