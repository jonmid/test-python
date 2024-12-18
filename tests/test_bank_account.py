import unittest, os

from unittest.mock import patch
from src.exceptions import InsufficientFundsError, WithdrawalTimeRestrictionError
from src.bank_account import BankAccount


class BankAccountTests(unittest.TestCase):

    # Se ejecuta antes de iniciar las pruebas
    def setUp(self) -> None:
        self.account = BankAccount(balance=1000, log_file="transaction_log.txt")

    # Se ejecuta después de terminar cada test
    def tearDown(self) -> None:
        if os.path.exists(self.account.log_file):
            os.remove(self.account.log_file)

    def _count_lines(self, filename):
        with open(filename, "r") as f:
            return len(f.readlines())
    
    # ************************************************

    def test_deposit_increases_balance_by_deposit_amount(self):
        new_balance = self.account.deposit(500)
        self.assertEqual(new_balance, 1500, "The balance sheet is not equal")

    @patch("src.bank_account.datetime")
    def test_withdraw_decreases_balance_by_withdraw_amount(self, mock_datetime):
        mock_datetime.now.return_value.hour = 15 
        new_balance = self.account.withdraw(200)
        self.assertEqual(new_balance, 800, "The balance sheet is not equal")

    def test_get_balance_returns_current_balance(self):
        self.assertEqual(self.account.get_balance(), 1000)

    def test_deposit_logs_transaction(self):
        self.account.deposit(500)
        self.assertTrue(os.path.exists("transaction_log.txt"))

    def test_withdraw_logs_each_transaction(self):
        self.assertEqual(self._count_lines(self.account.log_file), 1)
        self.account.deposit(500)
        self.assertEqual(self._count_lines(self.account.log_file), 2)
    
    @patch("src.bank_account.datetime")
    def test_withdraw_raises_error_when_insufficient_funds(self, mock_datetime):
        mock_datetime.now.return_value.hour = 10
        with self.assertRaises(InsufficientFundsError):
            self.account.withdraw(2000)
    
    @patch("src.bank_account.datetime")
    def test_withdraw_during_business_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 8
        new_balance = self.account.withdraw(100)
        self.assertEqual(new_balance, 900)

    @patch("src.bank_account.datetime")
    def test_withdraw_disallow_before_business_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 7
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.account.withdraw(100)

    @patch("src.bank_account.datetime")
    def test_withdraw_disallow_after_business_hours(self, mock_datetime):
        mock_datetime.now.return_value.hour = 18
        with self.assertRaises(WithdrawalTimeRestrictionError):
            self.account.withdraw(100)
    
    # Test con multiples valores.
    # Este caso prueba el método "deposit" con múltiples valores usando "subTest".
    def test_deposit_multiple_amounts(self):
        test_cases = [
            {"amount": 100, "expected": 1100},
            {"amount": 3000, "expected": 4000},
            {"amount": 4500, "expected": 5500},
        ]

        for case in test_cases:
            with self.subTest(case=case):
                self.account = BankAccount(balance=1000, log_file="transaction_log.txt")
                new_balance = self.account.deposit(case["amount"])
                self.assertEqual(new_balance, case["expected"])
