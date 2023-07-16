from bank import MockBank
from atm import ATM, ATMController
import unittest

class ATMControllerTest(unittest.TestCase):
    def setUp(self):
        self.bank = MockBank()
        self.atm = ATM(self.bank)
        self.atm_controller = ATMController(self.atm)

    def test_insert_card(self):
        result = self.atm_controller.insert_card("123456")
        self.assertEqual(result, "Your card has been successfully inserted")

    def test_enter_pin(self):
        self.atm_controller.insert_card("123456")
        result = self.atm_controller.enter_pin(1234)
        self.assertEqual(result, "PIN number entered successfully")

    def test_get_accounts_list(self):
        self.atm_controller.insert_card("123456")
        result = self.atm_controller.get_accounts_list()
        self.assertEqual(result, ["account1", "account2"])

    def test_select_account(self):
        self.atm_controller.insert_card("123456")
        self.atm_controller.get_accounts_list()
        result = self.atm_controller.select_account("account1")
        self.assertEqual(result, "Account has been successfully selected")

    def test_check_balance(self):
        self.atm_controller.insert_card("123456")
        self.atm_controller.get_accounts_list()
        self.atm_controller.select_account("account1")
        result = self.atm_controller.check_balance()
        self.assertEqual(result, 5000)

    def test_deposit_money(self):
        self.atm_controller.insert_card("123456")
        self.atm_controller.get_accounts_list()
        self.atm_controller.select_account("account1")
        result = self.atm_controller.deposit_money(1000)
        self.assertEqual(result, "Deposit has been processed")

    def test_withdraw_money(self):
        self.atm_controller.insert_card("123456")
        self.atm_controller.get_accounts_list()
        self.atm_controller.select_account("account1")
        result = self.atm_controller.withdraw_money(3000)
        self.assertEqual(result, "Withdrawal has been processed")

if __name__ == '__main__':
    unittest.main()

# if hard to understand unittest, use this
# def test_ATMController():
    
#     bank = MockBank()
#     atm = ATM(bank)
#     atm_controller = ATMController(atm)

#     result = atm_controller.insert_card("654321")
#     assert result == "Your card has been successfully inserted"

#     result = atm_controller.enter_pin(4321)
#     assert result == "PIN number entered successfully"
    
#     result = atm_controller.get_accounts_list()
#     assert result == ["account1", "account2"]
   
#     result = atm_controller.select_account("account1")
#     assert result == "Account has been successfully selected"
  
#     result = atm_controller.check_balance()
#     assert result == 3000
   
#     result = atm_controller.deposit_money(1000)
#     assert result == "Deposit has been processed"
  
#     result = atm_controller.withdraw_money(3000)
#     assert result == "Withdrawal has been processed"

# test_ATMController()
