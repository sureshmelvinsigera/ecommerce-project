import sys

from PyInquirer import prompt
from prettytable import PrettyTable

from product import Product
from datastorage import DataStorage
from main import Menu


class Admin:
    """

    """
    __ecommerce_data = DataStorage.ecommerce_data  # all the data

    def __init__(self):
        self.__products_table = PrettyTable()
        self.__sellers_table = None
        self.__customers_table = None

    def show_all_sellers(self):
        """
        print all the sellers
        """
        self.__sellers_table = PrettyTable()
        self.__sellers_table.title = 'All sellers'
        self.__sellers_table.field_names = ["Seller full name", "Store name"]
        self.__sellers_table.align = "l"
        for key, values in Admin.__ecommerce_data.items():
            for k, v in values.items():
                if v == 'seller':
                    self.__sellers_table.add_row(
                        [values['first_name'] + " " + values['last_name'], values['store_name']])
        print(self.__sellers_table)

    def show_all_customers(self):
        """
        print all the customers
        """
        self.__customers_table = PrettyTable()
        self.__customers_table.title = 'All customers'
        self.__customers_table.field_names = ["Customer full name", "EMail address"]
        self.__customers_table.align = "l"
        for key, values in Admin.__ecommerce_data.items():
            for k, v in values.items():
                if v == 'customer':
                    self.__customers_table.add_row(
                        [values['first_name'] + " " + values['last_name'], values['email']])
        print(self.__customers_table)

    def site_admin(self, account_number):
        while True:
            admin_menu = [
                {
                    'type': 'list',
                    'name': 'admin-menu-selection',
                    'message': 'Admin Menu',
                    'choices': [
                        'Show all products', 'Add product', 'Edit product', 'Delete product',
                        'Show all sellers', 'Show customers', 'Logout'
                    ]
                }
            ]

            product = Product()
            admin_menu_selection = prompt(admin_menu)
            if admin_menu_selection['admin-menu-selection'] == 'Show all products':
                product.show_all_products(account_number)
            if admin_menu_selection['admin-menu-selection'] == 'Add product':
                product.add_product(account_number)
            if admin_menu_selection['admin-menu-selection'] == 'Edit product':
                product.update_product(account_number)
            if admin_menu_selection['admin-menu-selection'] == 'Delete product':
                product.delete_product(account_number)
            if admin_menu_selection['admin-menu-selection'] == 'Show all sellers':
                self.show_all_sellers()
            if admin_menu_selection['admin-menu-selection'] == 'Show customers':
                self.show_all_customers()
            if admin_menu_selection['admin-menu-selection'] == 'Logout':
                menu = Menu()
                menu.user_login_menu()
