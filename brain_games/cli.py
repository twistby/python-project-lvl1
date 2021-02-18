"""cli.py module."""
import prompt


def welcome_user():
    """Welcome user."""
    print('Welcome to the Brain Games!')


def ask_user_name():
    """Ask and returns user name."""
    name = prompt.string('May I have your name? ')
    print('Hello, {user_name}!'.format(user_name=name))
    return name


def pr_str(p_string):
    """Print something."""
    print(p_string)


def pr_wrong_answ(answer, right_answer):
    """Print text when wrong answer."""
    msg1 = "'{a}' is wrong answer ;(. Correct answer".format(a=answer)
    msg2 = " was '{ra}'.".format(ra=right_answer)
    print(msg1 + msg2)


def ask(question):
    """Ask answer."""
    return prompt.string(question)


def end_game(user_name, user_win):
    """Show game result."""
    if user_win:
        print('Congratulations, {user_name}!'.format(user_name=user_name))
    else:
        print("Let's try again, {user_name}!".format(user_name=user_name))
