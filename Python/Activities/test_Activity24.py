import pytest


# add fixture
@pytest.fixture
def wallet():
    amount = 0
    return amount


# parameterized test
@pytest.mark.parametrize("earned, spent, expected", [(30, 10, 20), (20, 2, 18)])
def test_wallet(wallet, earned, spent, expected):
    # add money to wallet
    wallet = wallet + earned
    # remove money from wallet
    wallet = wallet - spent
    assert wallet == expected

