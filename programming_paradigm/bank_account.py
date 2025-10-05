# bank_account.py

from typing import Union

class InvalidAmountError(ValueError):
    """Raised when an amount is invalid (non-numeric or non-positive)."""

class InsufficientFundsError(Exception):
    """Raised when a withdrawal is attempted but funds are insufficient."""

class BankAccount:
    """Simple bank account with encapsulated balance and safe deposit/withdraw."""

    def __init__(self, initial_balance: Union[int, float] = 0):
        try:
            self._balance = float(initial_balance)
        except (TypeError, ValueError):
            raise InvalidAmountError("Initial balance must be numeric.")
        if self._balance < 0:
            raise InvalidAmountError("Initial balance cannot be negative.")

    @property
    def balance(self) -> float:
        """Read-only balance property (encapsulation)."""
        return self._balance

    def deposit(self, amount: Union[int, float]):
        """Deposit a positive numeric amount."""
        try:
            amt = float(amount)
        except (TypeError, ValueError):
            raise InvalidAmountError("Deposit amount must be numeric.")
        if amt <= 0:
            raise InvalidAmountError("Deposit amount must be greater than 0.")
        self._balance += amt

    def withdraw(self, amount: Union[int, float]) -> bool:
        """Withdraw a positive amount if funds suffice; raises on invalid input or insufficient funds."""
        try:
            amt = float(amount)
        except (TypeError, ValueError):
            raise InvalidAmountError("Withdrawal amount must be numeric.")
        if amt <= 0:
            raise InvalidAmountError("Withdrawal amount must be greater than 0.")
        if amt > self._balance:
            raise InsufficientFundsError("Insufficient funds.")
        self._balance -= amt
        return True

    def display_balance(self):
        """Print the current balance formatted."""
        print(f"Current Balance: ${self._balance:.2f}")
