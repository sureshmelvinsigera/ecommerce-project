from PyInquirer import prompt
from prettytable import PrettyTable

from product import Product
from datastorage import DataStorage
from menu import Menu
from product import Product


class Customer:
    """

    """
    __ecommerce_data = DataStorage.ecommerce_data  # all the data

    def __init__(self):
        self.__products_table = PrettyTable()

    def customer_admin(self, account_number):
        """

        """
        while True:
            customer_menu = [
                {
                    'type': 'list',
                    'name': 'customer-menu-selection',
                    'message': 'customer Menu',
                    'choices': [
                        'Show all products', 'Shopping Cart', 'Orders', 'Payment methods', 'Logout'
                    ]
                }
            ]

            product = Product()
            seller_menu_selection = prompt(customer_menu)
            if seller_menu_selection['customer-menu-selection'] == 'Show all products':
                product.show_all_products()
