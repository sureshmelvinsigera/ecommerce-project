__author__ = "Suresh Melvin Sigera"
__copyright__ = "Copyright 2021, The ESSEX Project"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Suresh Melvin Sigera"
__email__ = "sureshsigera@gmail.com"
__status__ = "Staging"

# import required dependencies
from payment_interface import PaymentInterface


class ECommercePaymentGateWay(PaymentInterface):
    """

    """

    def credit_card(self, purchase):
        card_number = input("Please enter the card number")

    def debit_card(self, sale):
        card_number = input("Please enter the card number")

    def paypal(self):
        card_number = input("Please enter the card number")
