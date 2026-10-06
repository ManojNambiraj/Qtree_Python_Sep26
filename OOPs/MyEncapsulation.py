# Encapsulation: (Getter & Setter)

    # Access Specifiers
        # Public
        # Private

class BankAccount:
    def __init__(self):
        self.__bankHolder = ""
        self.__bankBalance = 0

    def setBankHolder(self, name):
        self.__bankHolder = name

    def getBankHolder(self):
        return self.__bankHolder

    def setBankBalance(self, amt):
        self.__bankBalance = amt

    def getBankBalance(self):
        return self.__bankBalance

HDFC = BankAccount()

HDFC.setBankHolder("Savitha")
HDFC.setBankBalance(5000)

print(HDFC.getBankHolder())
print(HDFC.getBankBalance())

