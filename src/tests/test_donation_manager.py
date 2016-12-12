"""This is test module for donation_manager."""
import pytest

NEW_DONOR_TABLE = [
    ["sally jones", {"john smith": [10, 20, 30]}, {"john smith": [10, 20, 30], "sally jones": []}],
    ["john smith", {"john smith": [10, 20, 30]}, {"john smith": [10, 20, 30], "john smith": []}],
    ["Colin", {"colin": []}, {"colin": [], "Colin": []}]
]


HANDLE_DONATION_TABLE = [
    ["sally jones", 40, {"john smith": [10, 20, 30], "sally jones": []}, {"john smith": [10, 20, 30], "sally jones": [40]}],
    ["john smith", 2, {"john smith": [10, 20, 30], "sally jones": []}, {"john smith": [10, 20, 30, 2], "sally jones": []}],
    ["john smith", 10, {"john smith": [10, 20, 30], "santa claus": [20, 40]}, {"john smith": [10, 20, 30, 10], "santa claus": [20, 40]}],
    ["Colin", 20, {"colin": [], "Colin": []}, {"colin": [], "Colin": [20]}]
]


WRITE_EMAIL_TABLE = [
    ["sally jones", 40, {"john smith": [10, 20, 30], "sally jones": [40]}, "Thank you sally jones for your very generous donation of 40$"],
    ["john smith", 2, {"john smith": [10, 20, 30, 2], "sally jones": [10]}, "Thank you john smith for your very generous donation of 2$"],
    ["john smith", 10, {"john smith": [10, 20, 30, 10], "santa claus": [20, 40]}, "Thank you john smith for your very generous donation of 10$"],
    ["Colin", 20, {"joe": [30], "Colin": [20]}, "Thank you Colin for your very generous donation of 20$"]
]


CREATE_REPORT_TABLE = [
    [{"john smith": [10, 20, 30], "sally jones": [40]}, [100, 4, 25]],
    [{"john smith": [10, 20, 30, 20], "sally jones": [10]}, [90, 5, 18]],
    [{"john smith": [10, 20, 30, 10], "santa claus": [20, 30]}, [120, 6, 20]],
    [{"joe": [30], "Colin": [20, 30, 40, 50, 70]}, [240, 6, 40]],
]


SORTED_TABLE = [
    [
        [["Travis Walsh", 180, 7, 25], ["Nicholas Baker", 15, 2, 7], ["Kimberly Brown", 80, 5, 16]],
        [["Full Name", "Total Donations", "Number of Donations", "Average Donation"], ["Travis Walsh", 180, 7, 25], ["Kimberly Brown", 80, 5, 16], ["Nicholas Baker", 15, 2, 7]]
    ]
]


@pytest.mark.parametrize("user_input, dictionary, result", NEW_DONOR_TABLE)
def test_add_new_doner(user_input, dictionary, result):
    """Test send thanks when user adds a new name."""
    from donation_manager import add_new_donor
    assert add_new_donor(user_input, dictionary, ) == result


def test_enter_amount():
    """Test enter_amount function."""
    from donation_manager import enter_amount
    assert enter_amount("John", {"John": [40]}, 30) == 30.0


@pytest.mark.parametrize("user_name, amount, dictionary, result", HANDLE_DONATION_TABLE)
def test_handle_donation(user_name, amount, dictionary, result):
    """Test handle new donation amount added to dictionary."""
    from donation_manager import handle_donation
    assert handle_donation(user_name, dictionary, amount) == result


@pytest.mark.parametrize("user_name, amount, dictionary, result", WRITE_EMAIL_TABLE)
def test_write_email(user_name, amount, dictionary, result):
    """Test writing a string output that serves as an email."""
    from donation_manager import write_email
    assert write_email(user_name, amount, dictionary) == result


@pytest.mark.parametrize("dictionary, result", CREATE_REPORT_TABLE)
def test_create_report(dictionary, result):
    """Test create report function to build list of donors and amounts."""
    from donation_manager import create_report
    assert create_report(dictionary) == result


@pytest.mark.parametrize("list, result", SORTED_TABLE)
def test_print_report(list, result):
    """Test print_report function to sort the list."""
    from donation_manager import print_donor_report
    assert print_donor_report(list) == result
