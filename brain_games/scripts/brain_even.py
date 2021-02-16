"""Brain even script."""
import random

import prompt


def game_body():
    """Game circle. # noqa: DAR201."""
    for _ in range(3):
        current_number = random.randint(1, 1000)
        right_answer = 'yes' if current_number % 2 == 0 else 'no'
        print('Question: {cn}'.format(cn=current_number))
        answer = prompt.string('Your answer: ')
        if answer == right_answer:
            print('Correct!')
        else:
            msg1 = "'{a}' is wrong answer ;(. Correct answer".format(a=answer)
            msg2 = " was '{r}'.".format(r=right_answer)
            print(msg1 + msg2)
            return False
    return True


def main():
    """Start of script."""
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print('Hello, {user_name}!'.format(user_name=user_name))
    print('Answer "yes" if the number is even, otherwise answer "no".')
    if game_body():
        print('Congratulations, {user_name}!'.format(user_name=user_name))
    else:
        print("Let's try again, {user_name}!".format(user_name=user_name))


if __name__ == '__main__':
    main()
