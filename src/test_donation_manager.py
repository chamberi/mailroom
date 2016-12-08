"""This is test module for donation_manager."""
import pytest

THANKS_TABLE = [
    ["q", "quitting"],
    ["Q", "quitting"],
    ["quit", "quitting"],
    ["QUIT", "quitting"],
    ["Quit", "quitting"],
    ["list", "printing list"],
    ["LIST", "printing list"],
    ["List", "printing list"],
]


@pytest.mark.parametrize("response, result", THANKS_TABLE)
def test_send_thanks(response, result):
    """Test send thanks."""
    from donation_manager import send_thanks
    assert send_thanks(response) == result
