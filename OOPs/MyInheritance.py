# Inheritance

# Example 1:

    # class GrandParent:
    #     assetsValue = 20000000

    # class Parent(GrandParent):
    #     bankBalance = 500000

    #     def behaviour(self):
    #         print("Always having a smiling face")

    # class Child(Parent):
    #     pocketMoney = 500

    # sam = Child()

    # print(sam.pocketMoney)
    # print(sam.bankBalance)
    # sam.behaviour()
    # print(sam.assetsValue)

# Example 2:

class Parent:
    def __init__(self, amount):
        self.bankBalance = 500000
        self.childs_PocketMoney = amount

    def manageBankBalance(self):
        self.bankBalance -= self.childs_PocketMoney
        print("Parents bank balance: ", self.bankBalance)

class Child(Parent):
    def __init__(self, amt):
        super().__init__(amt)

sam = Child(200)

print("PocketMoney", sam.childs_PocketMoney)
sam.manageBankBalance()




