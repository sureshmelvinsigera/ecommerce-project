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

from product import Product
from datastorage import DataStorage
from main import Menu
from searchdatastorage import ProductSearch


class Seller:
    """
    This class provides utility methods seller related tasks.
    """
    # load local data storage
    __ecommerce_data = DataStorage.ecommerce_data

    def __init__(self):
        self.__products_table = PrettyTable()

    def seller_admin(self, account_number):
        """
        If the current logged in user is a seller, then load the load the seller admin interface
        :param account_number:
        :return:
        """
        while True:
            seller_menu = [
                {
                    'type': 'list',
                    'name': 'seller-menu-selection',
                    'message': 'Seller Menu',
                    'choices': [
                        'Product search',
                        'Show all products',
                        'Add product',
                        'Edit product',
                        'Delete product',
                        'Logout'
                    ]
                }
            ]

            product = Product()
            seller_menu_selection = prompt(seller_menu)

            # If the user selection is product search
            if seller_menu_selection['seller-menu-selection'] == 'Product search':
                keyword = input("Please enter any keyword: ")
                # create new search object
                product_search = ProductSearch()
                product_search.search_products(keyword)
            # If the user selection is to see all the products that belongs to them
            if seller_menu_selection['seller-menu-selection'] == 'Show all products':
                product.show_all_products(account_number)
            # If the user selection is to a add new product
            if seller_menu_selection['seller-menu-selection'] == 'Add product':
                product.add_product(account_number)
            # If the user selection is to edit an existing product
            if seller_menu_selection['seller-menu-selection'] == 'Edit product':
                product.update_product(account_number)
            # If the user selection is to delete an existing product
            if seller_menu_selection['seller-menu-selection'] == 'Delete product':
                product.delete_product(account_number)
            # if the user decided to logout, then show the main menu
            if seller_menu_selection['seller-menu-selection'] == 'Logout':
                menu = Menu()
                menu.user_login_menu()
