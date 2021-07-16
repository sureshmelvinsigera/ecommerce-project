import sys

from PyInquirer import prompt
from prettytable import PrettyTable

from product import Product
from datastorage import DataStorage
from main import Menu
from searchdatastorage import ProductSearch


class Seller:
    """

    """
    __ecommerce_data = DataStorage.ecommerce_data  # all the data

    def __init__(self):
        """

        """
        self.__products_table = PrettyTable()

    def seller_admin(self, account_number):
        """

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

            if seller_menu_selection['seller-menu-selection'] == 'Product search':
                keyword = input("Please enter any keyword: ")
                product_search = ProductSearch()
                product_search.search_products(keyword)
            if seller_menu_selection['seller-menu-selection'] == 'Show all products':
                product.show_all_products(account_number)
            if seller_menu_selection['seller-menu-selection'] == 'Add product':
                product.add_product(account_number)
            if seller_menu_selection['seller-menu-selection'] == 'Edit product':
                product.update_product(account_number)
            if seller_menu_selection['seller-menu-selection'] == 'Delete product':
                product.delete_product(account_number)
            if seller_menu_selection['seller-menu-selection'] == 'Logout':
                menu = Menu()
                menu.user_login_menu()
