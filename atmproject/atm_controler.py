from atm import ATM
from bank import Bank

class ATMController:
    def __init__(self, atm: ATM):
        self.atm = atm

    def insert_card(self, card_number: str) -> str:
        try:
            self.atm.insert_card(card_number)
            return "카드가 정상적으로 삽입되었습니다."
        except ValueError as e:
            return str(e)

    def enter_pin(self, pin: str) -> str:
        try:
            self.atm.enter_pin(pin)
            return "PIN 번호가 정상적으로 입력되었습니다."
        except ValueError as e:
            return str(e)

    def get_account_list(self) -> list:
        try:
            return self.atm.get_account_list()
        except ValueError as e:
            return str(e)

    def select_account(self, account_name: str) -> str:
        try:
            self.atm.select_account(account_name)
            return "계좌가 정상적으로 선택되었습니다."
        except ValueError as e:
            return str(e)

    def check_balance(self) -> int:
        try:
            return self.atm.check_balance()
        except ValueError as e:
            return str(e)

    def deposit_money(self, amount: int) -> str:
        try:
            self.atm.deposit_money(amount)
            return "입금이 정상적으로 처리되었습니다."
        except ValueError as e:
            return str(e)

    def withdraw_money(self, amount: int) -> str:
        try:
            self.atm.withdraw_money(amount)
            return "출금이 정상적으로 처리되었습니다."
        except ValueError as e:
            return str(e)
