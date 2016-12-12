"""This is an implementation of a mailroom manager."""
from __future__ import print_function
import math
from tabulate import tabulate
DONORS_DICT = {
    "Wesley Brown": [10, 20, 30],
    "Sally Jones": [40, 10, 50],
    "Samantha Gross": [5, 10, 5, 20, 40],
    "Brittany Foster": [25, 25, 30, 25, 25, 20, 30],
    "Tom Valenzuela": [5, 10]
}


def original_prompt(dictionary):
    """Navigate our script."""
    while True:
        print("To quit, enter q or quit.")
        user_choice = input("do you want to a: 'Send a Thank You?' or b:'Create a Report'? ")
        if user_choice.lower() == 'q':
            return
        elif user_choice == 'a':
            enter_full_name(dictionary)
        elif user_choice == 'b':
            create_report(dictionary)


def create_report(dictionary):
    """Create a list with name, total, number and average donations."""
    big_total = 0
    big_times = 0
    big_average = 0
    donor_list = []
    for name in dictionary:
        total = sum(dictionary[name])
        big_total += total
        times = len(dictionary[name])
        big_times += times
        average = math.floor(total / times)
        donor_list.append([name, total, times, average])
    big_average = math.floor(big_total / big_times)
    print_donor_report(donor_list)
    return [big_total, big_times, big_average]


def print_donor_report(lst):
    """Sort the donor list and print it out in a table format."""
    new_list = sorted(lst, key=lambda x: x[1], reverse=True)
    new_list.insert(0, ["Full Name", "Total Donations", "Number of Donations", "Average Donation"])
    print(tabulate(new_list))
    return new_list


def enter_full_name(dictionary):
    """Prompt the user to enter a donor name."""
    user_input = input('Enter a Full Name or List for a list of current donors: ')
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
        amount_prompt(user_input, dictionary)
    else:
        amount_prompt(user_input, dictionary)


def add_new_donor(user_input, dictionary):
    """Add a new donor key to our dictionary."""
    dictionary[user_input] = []
    return dictionary


def amount_prompt(user_input, dictionary):
    """Prompt user for a donation amount."""
    amount_input = input('Enter a donation amount: ')
    enter_amount(user_input, dictionary, amount_input)


def enter_amount(user_input, dictionary, donation_amount):
    """Prompt for a donation amount."""
    try:
        donation = float(donation_amount)
        handle_donation(user_input, dictionary, donation)
        return donation
    except ValueError:
        if donation_amount.lower() == 'q':
            return original_prompt(dictionary)
        return amount_prompt(user_input, dictionary)


def handle_donation(user_input, dictionary, donation_amount):
    """Add donation to dictionary."""
    dictionary[user_input].append(donation_amount)
    write_email(user_input, donation_amount, dictionary)
    return dictionary


def write_email(user_input, donation_amount, dictionary):
    """Write more tests."""
    output = "Thank you {} for your very generous donation of {}$".format(user_input, donation_amount)
    print(output)
    return output


if __name__ == '__main__':
    original_prompt(DONORS_DICT)  # pragma: no cover
