__author__ = "Suresh Melvin Sigera"
__copyright__ = "Copyright 2021, The ESSEX Project"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Suresh Melvin Sigera"
__email__ = "sureshsigera@gmail.com"
__status__ = "Staging"

# import required dependencies
import sys

from PyInquirer import prompt


class Menu:
    """
    This class provides main utility methods for the driver codes
    """

    @staticmethod
    def user_login_menu():
        """
        This static method generates the user login, register and exit functionality.
        :return:
        """
        # menu consists of login, register and exit
        user_login = [
            {
                'type': 'list',
                'name': 'user-login-selection',
                'message': 'User Login',
                'choices': [
                    'Login',
                    'Register',
                    'Exit'
                ]
            }
        ]

        user_login_result = prompt(user_login)
        if user_login_result['user-login-selection'] == 'Login':
            from user import User
            # create new user instance
            system_user = User()
            user_id = int(input("Please enter the user id: "))
            password = input("Please enter the password: ")
            system_user.login(user_id, password)
            # system_user.login(10000, "UDwh&AWD72g21")
            # system_user.login(10001, "UDwh&AWD72g22")
            # system_user.login(10003, "UDwh&AWD72g23")
        if user_login_result['user-login-selection'] == 'Register':
            from user import User
            # create new user instance
            system_user = User()
            system_user.create_user()
        if user_login_result['user-login-selection'] == 'Exit':
            # exit the program
            sys.exit(0)


if __name__ == '__main__':
    # main driver
    menu = Menu()
    menu.user_login_menu()
