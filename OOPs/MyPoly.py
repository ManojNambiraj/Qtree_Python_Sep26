# Polymorphism:

class Payment:
    def pay(self):
        print("Making Payment")

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid Rs: {amount} Using Credit Card")

class UPI(Payment):
    def pay(self, amount):
        print(f"Paid Rs: {amount} Using UPI")

class Cash(Payment):
    def pay(self, amount):
        print(f"Paid Rs: {amount} Using Cash")

payments = [CreditCard(), UPI(), Cash()]

for payment in payments:
    payment.pay(1000)