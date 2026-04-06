import pytest
from basics.bank_account import BankAccount

@pytest.fixture
def account():
    return BankAccount("Chris", 1000.00)

def test_initial_balance(account):
    assert account.balance == 1000.00

def test_owner(account):
    assert account.owner == "Chris"

def test_deposit(account):
    account.deposit(500.00)
    assert account.balance == 1500.00

def test_withdraw(account):
    account.withdraw(200.00)
    assert account.balance == 800.00

def test_deposit_negative(account):
    with pytest.raises(ValueError):
        account.deposit(-100)

def test_withdraw_negative(account):
    with pytest.raises(ValueError):
        account.withdraw(-100)

def test_withdraw_insufficient_funds(account):
    with pytest.raises(ValueError):
        account.withdraw(2000)