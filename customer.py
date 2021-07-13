from PyInquirer import prompt
from prettytable import PrettyTable
from datastorage import DataStorage
from main import Menu
from product import Product
from shoppingcart import ShoppingCart


class Customer:
    """

    """
    __ecommerce_data = DataStorage.ecommerce_data  # all the data

    def __init__(self):
        self.__products_table = PrettyTable()
        self.__shopping_cart = ShoppingCart()
        self.__account_number = None

    def customer_admin(self, account_number):
        self.__account_number = account_number
        """

        """
        while True:
            customer_menu = [
                {
                    'type': 'list',
                    'name': 'customer-menu-selection',
                    'message': 'customer Menu',
                    'choices': [
                        'Add to shopping cart', 'Show shopping cart', 'Checkout', 'Logout'
                    ]
                }
            ]

            product = Product()
            customer_menu_selection = prompt(customer_menu)

            if customer_menu_selection['customer-menu-selection'] == 'Add to shopping cart':
                product.show_all_products()
                # selection_id = input("Please enter the sku: ")
                # selection_qty = int(input("Please enter the qty: "))
                # self.__shopping_cart.add_to_cart(selection_id, selection_qty)
                self.__shopping_cart.add_to_cart("su1003", 1)
                self.__shopping_cart.add_to_cart("jo1007", 2)
                self.__shopping_cart.add_to_cart("jo1005", 1)
            if customer_menu_selection['customer-menu-selection'] == 'Show shopping cart':
                self.__shopping_cart.show_cart()
            if customer_menu_selection['customer-menu-selection'] == 'Checkout':
                self.__shopping_cart.check_out(self.__account_number)
            if customer_menu_selection['customer-menu-selection'] == 'Logout':
                menu = Menu()
                menu.user_login_menu()
