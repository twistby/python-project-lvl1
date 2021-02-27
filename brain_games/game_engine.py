"""Brain games body."""
import prompt

ANSWERS_TO_WIN = 3


def play(game):
    """Play the game."""
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {user}!'.format(user=user_name))
    print(game.RULES)
    for _ in range(ANSWERS_TO_WIN):
        question, right_answer = game.get_question_and_answer()
        print('Question: {q}'.format(q=question))
        answer = prompt.string('Your answer: ')
        if answer == right_answer:
            print('Correct!')
        else:
            print("'{a}' is wrong answer ;(. Correct answer was '{ra}'.".format(
                a=answer,
                ra=right_answer))
            print("Let's try again, {user}!".format(user=user_name))
            return
    print('Congratulations, {user}!'.format(user=user_name))
