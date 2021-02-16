"""cli.py module."""
import prompt


def welcome_user():
    """Ask a user name."""
    name = prompt.string('May I have your name? ')
    print('Hello, {user_name}!'.format(user_name=name))
