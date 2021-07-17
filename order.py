__author__ = "Suresh Melvin Sigera"
__copyright__ = "Copyright 2021, The ESSEX Project"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Suresh Melvin Sigera"
__email__ = "sureshsigera@gmail.com"
__status__ = "Staging"

# import required dependencies
from PyInquirer import prompt

from datastorage import DataStorage


class Order:
    """
    This class provides utility methods order related tasks.
    """
    # load local data storage
    __ecommerce_data = DataStorage.ecommerce_data
    # to indicate current cart status
    status = None

    @staticmethod
    def process_order(account_number,
                      customer_record,
                      customer_address,
                      customer_cc,
                      seller_id,
                      check_out_sku,
                      pos,
                      check_out_qty,
                      check_out_price,
                      check_out_product_name):
        """
        This method obtains all the required user information from the ShoppingCart class in order to process the order.
        This Class is also responsible for checking the following bases-cases:
        1. User might try  to check out an empty cart
        2. User add products to the shopping cart, and decided to proceed to the order page, but then decided to add
           a product. Therefore, the system must maintain the state.
        3. User completed all the required steps to process the order, and visits the checkout page,
           Therefore, the system must maintain the shopping cart state.
        :param account_number:
        :param customer_record:
        :param customer_address:
        :param customer_cc:
        :param seller_id:
        :param check_out_sku:
        :param pos:
        :param check_out_qty:
        :param check_out_price:
        :param check_out_product_name:
        :return:
        """
        order_menu = [
            {
                'type': 'list',
                'name': 'order_menu-selection',
                'message': 'Would you like to proceed ?',
                'choices': [
                    'Yes',
                    'No'
                ]
            }
        ]

        order_menu_selection = prompt(order_menu)
        # if the user decided to check out the current order
        if order_menu_selection['order_menu-selection'] == 'Yes':
            if len(check_out_sku) == 0:
                # if the user decided to check out an empty shopping cart, then handle this base-case
                print("Your shopping basket is empty")
                # update the state, so the shopping cart class is aware of it
                Order.status = "Empty"
            else:
                # the shopping cart is not empty, look up seller by ids
                for i in range(len(seller_id)):
                    # retrieve the seller record
                    record = Order.__ecommerce_data.get(seller_id[i])
                    # for each sku in the customer cart check if it's a match with the seller sku data list
                    for r in range(len(record["sku"])):
                        # check the added skus are available in the data storage
                        if check_out_sku[i] == record["sku"][r]:
                            # for debug purpose only
                            # print("Before ", Order.__ecommerce_data.get(seller_id[i])["stock"][r])
                            # update the new stock qty for each seller
                            Order.__ecommerce_data.get(seller_id[i])["stock"][r] = \
                                Order.__ecommerce_data.get(seller_id[i])["stock"][r] - check_out_qty[i]
                            # add order details to the seller account
                            import os
                            import base64
                            order_id = base64.b64encode(os.urandom(6)).decode('ascii')
                            print(order_id)
                            while order_id not in Order.__ecommerce_data.get(seller_id[i])["order_id"]:
                                Order.__ecommerce_data.get(seller_id[i])["order_id"].append(order_id)
                            Order.__ecommerce_data.get(seller_id[i])["order_customer_full_name"].append(
                                customer_record["first_name"] + " " + customer_record["last_name"])
                            Order.__ecommerce_data.get(seller_id[i])["order_customer_id"].append(account_number)
                            Order.__ecommerce_data.get(seller_id[i])["order_customer_product_name"].append(
                                check_out_product_name)
                            Order.__ecommerce_data.get(seller_id[i])["order_customer_sku"].append(check_out_sku)
                            Order.__ecommerce_data.get(seller_id[i])["order_customer_qty"].append(check_out_qty)
                            Order.__ecommerce_data.get(seller_id[i])["order_shipping_status"].append(
                                "Order is awaiting picking")
                            Order.__ecommerce_data.get(seller_id[i])["order_customer_price_per_unit"].append(
                                check_out_price)

                print("Your order has been successfully processed")
                # update the state, so the shopping cart class is aware of it
                Order.status = "Success"
        if order_menu_selection['order_menu-selection'] == 'No':
            # update the state, so the shopping cart class is aware of it
            Order.status = "No"
        # return the order status for later use
        return Order.status
