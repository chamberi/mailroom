"""This is test module for donation_manager."""
import pytest

NEW_DONOR_TABLE = [
    ["sally jones", {"john smith": [10, 20, 30]}, {"john smith": [10, 20, 30], "sally jones": []}],
    ["john smith", {"john smith": [10, 20, 30]}, {"john smith": [10, 20, 30], "john smith": []}],
    ["Colin", {"colin": []}, {"colin": [], "Colin": []}]
]


HANDLE_DONATION_TABLE = [
    ["sally jones", 40, {"john smith": [10, 20, 30]}, {"john smith": [10, 20, 30], "sally jones": [40]}],
    ["john smith", {"john smith": [10, 20, 30], "sally jones": []}, {"john smith": [10, 20, 30], "john smith": []}],
    ["john smith", {"john smith": [10, 20, 30], "sally jones": [20]}, {"john smith": [10, 20, 30], "john smith": [20, 40]}],
    ["Colin", {"colin": []}, {"colin": [], "Colin": []}]
]


@pytest.mark.parametrize("user_input, dictionary, result", NEW_DONOR_TABLE)
def test_add_new_doner(user_input, dictionary, result):
    """Test send thanks when user adds a new name."""
    from donation_manager import add_new_donor
    assert add_new_donor(user_input, dictionary) == result


@pytest.mark.parametrize("user_name, amount, dictionary, result", HANDLE_DONATION_TABLE)
def test_handle_donation(user_name, amount, dictionary, result):
    """Test handle new donation amount added to dictionary."""
    from donation_manager import handle_donation
    assert handle_donation(user_name, amount, dictionary) == result
