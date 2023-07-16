# Import Bank class from the bank module
from bank import Bank

# Define the class ATM which represents the ATM machine
class ATM:
    # Constructor for ATM class. It takes a Bank object as argument
    def __init__(self, bank: Bank):
        self.bank = bank
        self.card_number = None
        self.account_number = None

    # Method for inserting card. It validates the card_number with the bank
    def insert_card(self, card_number: str) -> None:
        if self.bank.validate_card(card_number):
            self.card_number = card_number
        else:
            raise ValueError("Invalid card")
        
    # Method for entering PIN. It validates the PIN with the bank
    def enter_pin(self, pin: str) -> None:
        if not self.bank.validate_pin(self.card_number, pin):
            raise ValueError("Invalid PIN")
        
    # Method for getting a list of accounts linked to the card
    def get_accounts_list(self) -> list:
        return self.bank.get_accounts(self.card_number)
    
    # Method for selecting an account. It validates if the account_name exists in the bank
    def select_account(self, account_name: str) -> None:
        if account_name not in self.bank.get_accounts(self.card_number):
            raise ValueError("Account does not exist")
        self.account_number = account_name

    # Method for checking the balance of the selected account
    def check_balance(self) -> int:
        return self.bank.get_balance(self.card_number, self.account_number)
    # Method for depositing money into the selected account
    def deposit_money(self, amount: int) -> None:
        self.bank.deposit(self.card_number, self.account_number, amount)

    # Method for withdrawing money from the selected account
    def withdraw_money(self, amount: int) -> None:
        self.bank.withdraw(self.card_number, self.account_number, amount)

# Define the class ATMController which controls the ATM machine
class ATMController:
    def __init__(self, atm: ATM):
        self.atm = atm

    def insert_card(self, card_number: str) -> str:
        try:
            self.atm.insert_card(card_number)
            return "Your card has been successfully inserted"
        except ValueError as e:
            return str(e)

    def enter_pin(self, pin: str) -> str:
        try:
            self.atm.enter_pin(pin)
            return "PIN number entered successfully"
        except ValueError as e:
            return str(e)

    def get_accounts_list(self) -> list:
        try:
            return self.atm.get_accounts_list()
        except ValueError as e:
            return str(e)

    def select_account(self, account_name: str) -> str:
        try:
            self.atm.select_account(account_name)
            return "Account has been successfully selected"
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
            return "Deposit has been processed"
        except ValueError as e:
            return str(e)

    def withdraw_money(self, amount: int) -> str:
        try:
            self.atm.withdraw_money(amount)
            return "Withdrawal has been processed"
        except ValueError as e:
            return str(e)