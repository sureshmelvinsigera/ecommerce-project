import time

from PyInquirer import prompt

from datastorage import DataStorage
from main import Menu
from admin import Admin
from seller import Seller
from customer import Customer

class User:
    __ecommerce_data = DataStorage.ecommerce_data  # all the data

    def __init__(self):
        self.record = None  # to store specific user record

    def login(self, account_number, password):
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
        create new user
        """
        create_account_menu = [
            {
                'type': 'list',
                'name': 'create_account_menu_selection',
                'message': 'Create new user',
                'choices': ['Seller', 'Customer']
            }
        ]
        new_user_result = prompt(create_account_menu)

        if new_user_result['create_account_menu_selection'] == 'Seller':
            last_used_id = sorted(User.__ecommerce_data.keys())[-1]
            new_id = int(last_used_id) + 1
            print('\nProvide the following information about the seller account:\n')
            store_name = input('Store name: ')
            first_name = input('First name: ')
            last_name = input('Last name: ')
            email = input('EMail address: ')
            password = input("Enter a password: ")
            User.__ecommerce_data[new_id] = {
                "store_name": store_name,
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'password': password,
                'type': 'seller'
            }

            print("Your account has been successfully created")
            for i in range(4, 0, -1):
                print(f"Returning to main menu in ... {i}", end="\r", flush=True)
                time.sleep(1)
            menu = Menu()
            menu.user_login_menu()

        if new_user_result['create_account_menu_selection'] == 'Customer':
            last_user_id = sorted(User.__ecommerce_data.keys())[-1]
            new_user_id = int(last_user_id) + 1
            first_name = input('First name: ')
            last_name = input('Last name: ')
            email = input('EMail address: ')
            password = input("Enter a password: ")
            User.__ecommerce_data[new_user_id] = {
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'password': password,
                'type': 'customer'
            }

            print("Your account has been successfully created")
            for i in range(4, 0, -1):
                print(f"Returning to main menu in ... {i}", end="\r", flush=True)
                time.sleep(1)
            menu = Menu()
            menu.user_login_menu()
