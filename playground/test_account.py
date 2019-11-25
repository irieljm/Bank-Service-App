import unittest
from account import display_balance, transfer

class TestDisplayBalance(unittest.TestCase):
    def test_first_user_correct_pin(self):
        displayed_amount = display_balance(1234, 'Marie')
        self.assertEqual(displayed_amount, 'This is your current amount of money: 2000')

    def test_first_user_incorrect_pin(self):
        incorrect_pin = 1111
        correct_user = 'Marie'
        result = display_balance(incorrect_pin, correct_user)
        self.assertEqual(result, 'Incorrect PIN!!!')

    def test_first_user_incorrect_pin(self):
        incorrect_pin = '1111'
        correct_user = 'Marie'
        result = display_balance(incorrect_pin, correct_user)
        self.assertEqual(result, 'Incorrect PIN!!!')

    def test_first_user_incorrect_pin(self):
        incorrect_pin = 'abcd'
        correct_user = 'Marie'
        result = display_balance(incorrect_pin, correct_user)
        self.assertEqual(result, 'Incorrect PIN!!!')

    'more tests as homework!!'  

class TestWithdrawMoney(unittest.TestCase):
    def test_xxx(self):
        'your homework'

class TestTransferMoney(unittest.TestCase):
    def test_transfer_money_first_user_correct_pin(self):
        pin = 1234
        sender = 'Marie'
        receiver = 'Michelle'
        money_to_transfer = 300
        result = 'The amount 300 Euro were transferred to Michelle. Your current balance is 1700.'
        updated_account = transfer(pin, sender, receiver, money_to_transfer)
        self.assertEqual(updated_account, result)


   ''' def test_transfer_money_first_user_correct_pin(self):
        pin = 2222
        sender = 'Michelle'
        receiver = 'Charlotte'
        money_to_transfer = 300
        result = 'The amount 300 Euro were transferred to Michelle. Your current balance is 1700.'
        updated_account = transfer(pin, sender, receiver, money_to_transfer)
        self.assertEqual(updated_account, result)'''


if __name__ == '__main__':
    unittest.main()
