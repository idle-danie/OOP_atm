from abc import ABC, abstractmethod
# This class represents the blueprint for any bank
class Bank(ABC):
    # Method to check if a card is valid
    @abstractmethod
    def validate_card(self, card_number: str) -> bool:
        pass

    # Method to verify the entered PIN
    @abstractmethod
    def validate_pin(self, card_number: str, pin: str) -> bool:
        pass

    # Method to retrieve all accounts associated with a card
    @abstractmethod
    def get_accounts(self, card_number: str) -> list:
        pass

    # Method to check balance of an account
    @abstractmethod
    def get_balance(self, card_number: str, account_number: str) -> int:
        pass

    # Method to deposit money into an account
    @abstractmethod
    def deposit(self, card_number, account_number: str, amount: int) -> None:
        pass
    # Method to withdraw money from an account
    @abstractmethod
    def withdraw(self, card_number, account_number: str, amount: int) -> None:
        pass

# MockBank is a basic bank for testing purposes
class MockBank(Bank):
    # MockBank has some predefined accounts for testing
    def __init__(self):
        self.accounts = {
            "123456": {"pin": 1234, "accounts": {"account1": 5000, "account2": 10000}},
            "654321": {"pin": 4321, "accounts": {"account1": 3000, "account2": 20000}}
        }
    
    def validate_card(self, card_number: str) -> bool:
        return card_number in self.accounts
 
    def validate_pin(self, card_number: str, pin: int) -> bool:
        return self.accounts[card_number]["pin"] == pin
    
    def get_accounts(self, card_number: str) -> list:
        return list(self.accounts[card_number]["accounts"].keys())

    def get_balance(self, card_number: str, account_name: str) -> int:
        return self.accounts[card_number]["accounts"][account_name]
    
    def deposit(self, card_number: str, account_name: str, amount: int) -> None:
        self.accounts[card_number]["accounts"][account_name] += amount

    def withdraw(self, card_number: str, account_name: str, amount: int) -> None:
        if self.accounts[card_number]["accounts"][account_name] < amount:
            raise ValueError("balance is insufficient")
        self.accounts[card_number]["accounts"][account_name] -= amount
