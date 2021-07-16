__author__ = "Suresh Melvin Sigera"
__copyright__ = "Copyright 2021, The ESSEX Project"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Suresh Melvin Sigera"
__email__ = "sureshsigera@gmail.com"
__status__ = "Staging"

# import required dependencies
import time

from PyInquirer import prompt

from datastorage import DataStorage
from main import Menu
from admin import Admin
from seller import Seller
from customer import Customer


class User:
    """
    This class provides utility methods to login users and crate new users in the local data storage.
    """
    __ecommerce_data = DataStorage.ecommerce_data  # load local data storage

    def __init__(self):
        self.record = None  # to store specific user instance

    def login(self, account_number, password):
        """
        This method validated the user credentials based on user id, and password, and then it will route the user
        to a specific user dashboard.
        :param account_number:
        :param password:
        :return:
        """
        # if the account number exist then retrieve the record
        if User.__ecommerce_data.get(account_number):
            # set the current record for validation
            self.record = User.__ecommerce_data.get(account_number)
            if self.record['password'] == password and self.record['type'] == "owner":
                # call admin main menu upon successful login
                admin = Admin()
                admin.site_admin(account_number)
            elif self.record['password'] == password and self.record['type'] == "seller":
                # call seller menu upon successful login
                seller = Seller()
                seller.seller_admin(account_number)
            elif self.record['password'] == password and self.record['type'] == "customer":
                # call customer menu upon successful login
                customer = Customer()
                customer.customer_admin(account_number)
            else:
                # incorrect password, set to record None for security reasons
                print("User name or password is incorrect")
                # site_menu = Menu()
                # site_menu.user_login_menu()
        else:
            print("Account not found")

    @staticmethod
    def create_user():
        """
        This method creates a new user object in the local data storage. User have a choice to register
        as a customer or a seller.
        :return:
        """
        create_account_menu = [
            {
                'type': 'list',
                'name': 'create_account_menu_selection',
                'message': 'Create new user',
                'choices': [
                    'Seller',
                    'Customer'
                ]
            }
        ]
        new_user_result = prompt(create_account_menu)

        # if the selection is seller
        if new_user_result['create_account_menu_selection'] == 'Seller':
            # obtain the last used id from the local data storage
            last_used_id = sorted(User.__ecommerce_data.keys())[-1]
            # generate the new user id
            new_id = int(last_used_id) + 1
            print('\nProvide the following information about the seller account:\n')
            store_name = input('Store name: ')
            first_name = input('First name: ')
            last_name = input('Last name: ')
            email = input('EMail address: ')
            password = input("Enter a password: ")
            # insert the new object to the local data storage
            User.__ecommerce_data[new_id] = {
                "store_name": store_name,
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'password': password,
                'sku': [],
                'products': [],
                'prices': [],
                'stock': [],
                'type': 'seller'
            }

            print("Your account has been successfully created")
            # return the user to login screen in 4 second count down
            for i in range(4, 0, -1):
                print(f"Returning to main menu in ... {i}", end="\r", flush=True)
                time.sleep(1)
            menu = Menu()
            menu.user_login_menu()

        # if the selection is customer
        if new_user_result['create_account_menu_selection'] == 'Customer':
            # obtain the last used id from the local data storage
            last_user_id = sorted(User.__ecommerce_data.keys())[-1]
            # generate new user id
            new_user_id = int(last_user_id) + 1
            first_name = input('First name: ')
            last_name = input('Last name: ')
            email = input('EMail address: ')
            password = input("Enter a password: ")
            # insert the new object to the local data storage
            User.__ecommerce_data[new_user_id] = {
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'password': password,
                'type': 'customer'
            }
            print("Your account has been successfully created")
            # return the user to login screen in 4 second count down
            for i in range(4, 0, -1):
                print(f"Returning to main menu in ... {i}", end="\r", flush=True)
                time.sleep(1)
            menu = Menu()
            menu.user_login_menu()
