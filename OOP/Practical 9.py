from abc import ABC, abstractmethod

# Create an abstract class
class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass
# Create a subclass that inherits from the abstract class
class CreditCardPayment(Payment):
    def __init__(self, card_number, card_holder):
        self.card_number=card_number
        self.card_holder=card_holder
    def process_payment(self, amount):
        return f"Processing credit card payment of {amount} for {self.card_holder}."
# Creating a subclass that inherits from the abstract class
class PayPalPayment(Payment):
    def __init__(self, email):
        self.email=email
    def process_payment(self, amount):
        return f"Processing paypal payment of {amount} for {self.email}."
# Create a subclass that inherits from the abstract class
class BankTransferPayment(Payment):
    def __init__(self, account_number, account_holder):
        self.account_number=account_number
        self.account_holder=account_holder
    def process_payment(self, amount):
        return f"Processing bank transfer of {amount} for {self.account_holder}."
# Creating instances of the different payment methods
credit_card_payment=CreditCardPayment("2121-5487-6589-8754", "Amit")
pay_pal_payment=PayPalPayment("ani20@gmail.com")
bank_transfer_payment=BankTransferPayment("8754522142", "Amit")
# Processing payment using different methods
print(credit_card_payment.process_payment(10000))
print(pay_pal_payment.process_payment(4510))
print(bank_transfer_payment.process_payment(1200))