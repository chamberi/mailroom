"""This is test module for donation_manager."""
import pytest

NEW_DONOR_TABLE = [
    ["sally jones", {"john smith": [10, 20, 30]}, {"john smith": [10, 20, 30], "sally jones": []}],
    ["john smith", {"john smith": [10, 20, 30]}, {"john smith": [10, 20, 30], "john smith": []}],
    ["Colin", {"colin": []}, {"colin": [], "Colin": []}]
]


@pytest.mark.parametrize("user_input, dictionary, result", NEW_DONOR_TABLE)
def test_add_new_donor(user_input, dictionary, result):
    """Test send thanks when user adds a new name."""
    from donation_manager import add_new_donor
    assert add_new_donor(user_input, dictionary) == result
