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
        self.shopping_cart = ShoppingCart()

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
                        'Add to shopping cart', 'Logout'
                    ]
                }
            ]

            product = Product()
            seller_menu_selection = prompt(customer_menu)

            if seller_menu_selection['customer-menu-selection'] == 'Add to shopping cart':
                product.show_all_products()
                selection_id = input("Please enter the sku: ")
                selection_qty = int(input("Please enter the qty: "))
                self.shopping_cart.add_to_cart(selection_id, selection_qty)
                # self.shopping_cart.add_to_cart("su1003", 1)
                # self.shopping_cart.add_to_cart("jo1007", 2)
                # self.shopping_cart.add_to_cart("jo1005", 1)
            if seller_menu_selection['customer-menu-selection'] == 'Logout':
                menu = Menu()
                menu.user_login_menu()
