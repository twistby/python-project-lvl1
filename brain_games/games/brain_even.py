"""Brain even script."""
import random

import prompt

from brain_games import cli


def game_body(round_number=3):
    """Game circle. Return True if win, False if lose."""
    cli.pr_str('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(round_number):
        current_number = random.randint(1, 1000)
        right_answer = 'yes' if current_number % 2 == 0 else 'no'
        cli.pr_str('Question: {cn}'.format(cn=current_number))
        answer = prompt.string('Your answer: ')
        if answer == right_answer:
            print('Correct!')
        else:
            cli.pr_wrong_answ(answer, right_answer)
            return False
    return True


def main():
    """Start of script."""
    cli.welcome_user()
    user_name = cli.ask_user_name()
    cli.end_game(user_name, game_body())


if __name__ == '__main__':
    main()
