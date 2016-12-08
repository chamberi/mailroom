"""This is test module for donation_manager."""
import pytest

LIST_TABLE = [
    ["sally jones", {"john smith": [10, 20, 30]}, {"john smith": [10, 20, 30], "sally jones": []}],
]


@pytest.mark.parametrize("user_input, dictionary, result", LIST_TABLE)
def test_send_thanks_new_name(user_input, dictionary, result):
    """Test send thanks when user adds a new name."""
    from donation_manager import send_thanks
    assert send_thanks(user_input, dictionary) == result
