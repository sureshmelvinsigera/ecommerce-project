__author__ = "Suresh Melvin Sigera"
__copyright__ = "Copyright 2021, The ESSEX Project"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Suresh Melvin Sigera"
__email__ = "sureshsigera@gmail.com"
__status__ = "Staging"

# import required dependencies
from PyInquirer import prompt
from prettytable import PrettyTable
from datastorage import DataStorage
from main import Menu
from product import Product
from shoppingcart import ShoppingCart
from searchdatastorage import ProductSearch


class Customer:
    """
    This class provides utility methods customer related tasks.
    """
    # load local data storage
    __ecommerce_data = DataStorage.ecommerce_data  # all the data

    def __init__(self):
        # crate blank product table and shopping cart for the user object
        self.__products_table = PrettyTable()
        self.__shopping_cart = ShoppingCart()
        self.__account_number = None

    def customer_admin(self, account_number):
        """
        If the current logged in user is a customer, then load the load the customer admin interface
        :param account_number:
        :return:
        """
        self.__account_number = account_number
        # customer adin menu
        while True:
            customer_menu = [
                {
                    'type': 'list',
                    'name': 'customer-menu-selection',
                    'message': 'Customer Menu',
                    'choices': [
                        'Product search',
                        'Add to shopping cart',
                        'Show shopping cart',
                        'Checkout',
                        'Logout'
                    ]
                }
            ]

            product = Product()
            customer_menu_selection = prompt(customer_menu)

            # If the user selection is product search
            if customer_menu_selection['customer-menu-selection'] == 'Product search':
                keyword = input("Please enter any keyword: ")
                # create new search object
                product_search = ProductSearch()
                product_search.search_products(keyword)
            # If the user decided add an item to the shopping cart
            if customer_menu_selection['customer-menu-selection'] == 'Add to shopping cart':
                product.show_all_products()
                # selection_id = input("Please enter the sku: ")
                # selection_qty = int(input("Please enter the qty: "))
                # self.__shopping_cart.add_to_cart(selection_id, selection_qty)
                self.__shopping_cart.add_to_cart("su1003", 1)
                # self.__shopping_cart.add_to_cart("jo1007", 2)
                # self.__shopping_cart.add_to_cart("jo1005", 1)
            # If the user decided to see the what's in the shopping cart
            if customer_menu_selection['customer-menu-selection'] == 'Show shopping cart':
                self.__shopping_cart.show_cart()
            # If the user decided to start the checkout process
            if customer_menu_selection['customer-menu-selection'] == 'Checkout':
                # crate a new instance of the shopping cart object for the current user
                self.__shopping_cart.check_out(self.__account_number)
            # if the user decided to logout, then show the main menu
            if customer_menu_selection['customer-menu-selection'] == 'Logout':
                menu = Menu()
                menu.user_login_menu()
