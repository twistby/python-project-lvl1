"""cli.py module."""
import prompt


def welcome_user():
    """Welcome user."""
    print('Welcome to the Brain Games!')


def get_user_name():
    """Get and return user name."""
    name = prompt.string('May I have your name? ')
    print('Hello, {user_name}!'.format(user_name=name))
    return name


def get_answer(question):
    """Get user answer."""
    return prompt.string(question)
