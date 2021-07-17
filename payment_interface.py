from abc import ABC, abstractmethod


class PaymentInterface(ABC):
    """
    This abstract class must be implement by the payment class by achiving inhertance.
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
