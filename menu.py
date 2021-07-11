import sys

from PyInquirer import prompt
from product import Product

class Menu:
   pass
    # def site_admin(self, account_number):
    #     while True:
    #         admin_menu = [
    #             {
    #                 'type': 'list',
    #                 'name': 'admin-menu-selection',
    #                 'message': 'Admin Menu',
    #                 'choices': [
    #                     'Show all products', 'Add product', 'Edit product', 'Delete product',
    #                     'Show all sellers', 'Show customers', 'Logout'
    #                 ]
    #             }
    #         ]
    #
    #         product = Product()
    #         admin_menu_selection = prompt(admin_menu)
    #         if admin_menu_selection['admin-menu-selection'] == 'Show all products':
    #             product.show_all_products(account_number)
    #         if admin_menu_selection['admin-menu-selection'] == 'Add product':
    #             product.add_product(account_number)
    #         if admin_menu_selection['admin-menu-selection'] == 'Edit product':
    #             product.update_product(account_number)
    #         if admin_menu_selection['admin-menu-selection'] == 'Delete product':
    #             product.delete_product(account_number)
    #         if admin_menu_selection['admin-menu-selection'] == 'Show all sellers':
    #             product.show_all_sellers()
    #         if admin_menu_selection['admin-menu-selection'] == 'Show customers':
    #             product.show_all_customers()
    #         if admin_menu_selection['admin-menu-selection'] == 'Logout':
    #             sys.exit(0)
