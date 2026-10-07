# Abstraction

from abc import ABC, abstractmethod

class BankAccount(ABC):
    @abstractmethod
    def cal_interest(self):
        pass

class SavingsAccount(BankAccount):
    def cal_interest(self):
        print("Saving Account: 40%")

class CurrentAccount(BankAccount):
    def cal_interest(self):
        print("Current Account: 0%")

savings = SavingsAccount()
current = CurrentAccount()

savings.cal_interest()
current.cal_interest()