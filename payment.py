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
    This class provides utility methods for payment-related tasks.
    """

    def credit_card(self, purchase):
        """
        Customers can pay with credit cards
        :param purchase:
        :return:
        """
        card_number = input("Please enter the card number")

    def debit_card(self, sale):
        """
        Customers can pay with debit cards
        :param sale:
        :return:
        """
        card_number = input("Please enter the card number")

    def paypal(self):
        """
        Customers can pay with 3rd payment gateway such as Paypal
        :return:
        """
        card_number = input("Please enter the card number")
