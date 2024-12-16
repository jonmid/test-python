import pytest

from src.bank_account import BankAccount


@pytest.mark.parametrize("amount, expected", [
    (100, 1100),
    (3000, 4000),
    (4500, 5500),
])
def test_deposit_multiple_amounts_pytest(amount, expected):
    account = BankAccount(balance=1000, log_file="transactions.txt")
    new_balance = account.deposit(amount)
    assert new_balance == expected
