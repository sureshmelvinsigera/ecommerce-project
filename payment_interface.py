from abc import ABC, abstractmethod


class PaymentInterface(ABC):
    """

    """

    @abstractmethod
    def credit_card(self, purchase):
        pass

    @abstractmethod
    def debit_card(self, sale):
        pass

    @abstractmethod
    def paypal(self):
        pass
