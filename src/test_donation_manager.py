"""This is test module for donation_manager."""
import pytest

THANKS_TABLE = [
    ["q", original_prompt()],
    ["Q", original_prompt()],
    ["quit", orginal_prompt()],
    ["QUIT", orginal_prompt()],
    ["Quit", orginal_prompt()],
    ["list", enter_full_name()],
    ["LIST", enter_full_name()],
    ["List", enter_full_name()],
]


@pytest.mark.parametrize("response, result", THANKS_TABLE)
def test_send_thanks(response, result):
    """Test send thanks."""
    from donation_manager import send_thanks
    assert send_thanks(response) == result
