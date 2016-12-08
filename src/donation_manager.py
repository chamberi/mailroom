"""This is an implementation of a mailroom manager."""
from __future__ import print_function
DONORS_DICT = {}


def original_prompt():
    """Navigate our script."""
    while True:
        user_choice = input("do you want to a: 'Send a Thank You?' or b:'Create a Report'? ")
        if user_choice.lower() == 'q' or 'quit':
            return
        elif user_choice == 'a':
            enter_full_name()
        elif user_choice == 'b':
            return print("recreating full report")


def enter_full_name():
    """Prompt the user to enter a donor name."""
    user_input = input('Enter a Full Name: ')
    send_thanks(user_input)


def send_thanks(user_input, dictionary):
    """Send thanks."""
    if user_input.lower() == 'q' or user_input.lower() =='quit':
        original_prompt()
        return "quitting"
    elif user_input.lower() == "list":
        for name in dictionary:
            print(name)
            enter_full_name()
            return "printing list"
    elif user_input not in dictionary:
        dictionary[user_input] = []
        return dictionary
    else:
        return dictionary


def handle_donation():
    """Need to write more tests."""
    print("write more tests.")
