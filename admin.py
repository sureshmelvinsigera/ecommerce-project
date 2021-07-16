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
from orderstatus import OrderStatus


class Admin:
    """
    This class provides utility methods admin related tasks.
    """
    # load local data storage
    __ecommerce_data = DataStorage.ecommerce_data

    def __init__(self):
        self.__products_table = PrettyTable()
        self.__sellers_table = None
        self.__customers_table = None

    def show_all_sellers(self):
        """
        print all the sellers
        :return:
        """
        self.__sellers_table = PrettyTable()
        self.__sellers_table.title = 'All sellers'
        self.__sellers_table.field_names = ["Seller full name", "Email address"]
        self.__sellers_table.align = "l"
        # load all the data from local storage
        for key, values in Admin.__ecommerce_data.items():
            for k, v in values.items():
                # load only sellers
                if v == 'seller':
                    # generate the table with required attributes
                    self.__sellers_table.add_row(
                        [values['first_name'] + " " + values['last_name'], values['email']])
        print(self.__sellers_table)

    def show_all_customers(self):
        """
        print all the customers
        :return:
        """
        self.__customers_table = PrettyTable()
        self.__customers_table.title = 'All customers'
        self.__customers_table.field_names = ["Customer full name", "Email address"]
        self.__customers_table.align = "l"
        # load all the data from local storage
        for key, values in Admin.__ecommerce_data.items():
            for k, v in values.items():
                # load only sellers
                if v == 'customer':
                    # generate the table with required attributes
                    self.__customers_table.add_row(
                        [values['first_name'] + " " + values['last_name'], values['email']])
        print(self.__customers_table)

    def site_admin(self, account_number):
        """
        If the current logged in user is a customer, then load the load the customer admin interface
        :param account_number:
        :return:
        """
        while True:
            admin_menu = [
                {
                    'type': 'list',
                    'name': 'admin-menu-selection',
                    'message': 'Admin Menu',
                    'choices': [
                        'Product search',
                        'Show all products',
                        'Add product',
                        'Edit product',
                        'Delete product',
                        'Show all sellers',
                        'Show customers',
                        'Current orders',
                        'Logout'
                    ]
                }
            ]

            product = Product()
            admin_menu_selection = prompt(admin_menu)
            # If the user selection is product search
            if admin_menu_selection['admin-menu-selection'] == 'Product search':
                keyword = input("Please enter any keyword: ")
                # create new search object
                product_search = ProductSearch()
                product_search.search_products(keyword)
            # If the user selection is to see all the products that belongs to them
            if admin_menu_selection['admin-menu-selection'] == 'Show all products':
                product.show_all_products(account_number)
            # If the user selection is to add a new product
            if admin_menu_selection['admin-menu-selection'] == 'Add product':
                product.add_product(account_number)
            # If the user selection is to update an existing product
            if admin_menu_selection['admin-menu-selection'] == 'Edit product':
                product.update_product(account_number)
            # If the user selection is to delete an existing product
            if admin_menu_selection['admin-menu-selection'] == 'Delete product':
                product.delete_product(account_number)
            # If the user selection is to see all the sellers
            if admin_menu_selection['admin-menu-selection'] == 'Show all sellers':
                self.show_all_sellers()
            # If the user selection is to see all the customers
            if admin_menu_selection['admin-menu-selection'] == 'Show customers':
                self.show_all_customers()
            if admin_menu_selection['admin-menu-selection'] == 'Current orders':
                order_status = OrderStatus()
                order_status.status()
            # if the user decided to logout, then show the main menu
            if admin_menu_selection['admin-menu-selection'] == 'Logout':
                menu = Menu()
                menu.user_login_menu()
