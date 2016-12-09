"""This is an implementation of a mailroom manager."""
from __future__ import print_function
DONORS_DICT = {}


def original_prompt(dictionary):
    """Navigate our script."""
    while True:
        user_choice = input("do you want to a: 'Send a Thank You?' or b:'Create a Report'? ")
        if user_choice.lower() == 'q':
            return
        elif user_choice == 'a':
            print(user_choice)
            enter_full_name(dictionary)
        elif user_choice == 'b':
            return print("recreating full report")


def enter_full_name(dictionary):
    """Prompt the user to enter a donor name."""
    user_input = input('Enter a Full Name: ')
    send_thanks(user_input, dictionary)


def send_thanks(user_input, dictionary):
    """Send thanks."""
    if user_input.lower() == 'q' or user_input.lower() == 'quit':
        original_prompt(dictionary)
        return "quitting"
    elif user_input.lower() == "list":
        for name in dictionary:
            print(name)
            enter_full_name(dictionary)
            return "printing list"
    elif user_input not in dictionary:
        add_new_donor(user_input, dictionary)
        enter_amount(user_input, dictionary)
    else:
        enter_amount(user_input, dictionary)


def add_new_donor(user_input, dictionary):
    """Add a new donor key to our dictionary."""
    dictionary[user_input] = []
    return dictionary


def enter_amount(user_input, dictionary):
    """Prompt for a donation amount."""
    donation_amount = input('Enter a donation amout: ')
    if donation_amount.lower() == 'q':
        return original_prompt(dictionary)
    try:
        donation = int(donation_amount)
        handle_donation(user_input, dictionary, donation)
    except ValueError:
        enter_amount(user_input, dictionary)


def handle_donation(user_input, dictionary, donation_amount):
    """Add donation to dictionary."""
    try:
        if donation_amount.lower() == 'q':
            original_prompt(dictionary)
    except AttributeError:
        dictionary[user_input].append(donation_amount)
        write_email(user_input, donation_amount, dictionary)
        return dictionary


def write_email(user_input, donation_amount, dictionary):
    """Write more tests."""
    output = "Thank you {} for your very generous donation of {}$".format(user_input, donation_amount)
    print(output)
    return output


if __name__ == '__main__':
    original_prompt(DONORS_DICT)
