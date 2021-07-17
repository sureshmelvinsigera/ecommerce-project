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


class OrderStatus:
    """
    This class provides utility methods admin related tasks.
    """
    # load local data storage
    __ecommerce_data = DataStorage.ecommerce_data

    @staticmethod
    def status(account_number):
        user_record = OrderStatus.__ecommerce_data.get(account_number)
        if len(user_record['order_customer_id']) == 0 or None:
            print("Sorry there are no orders for this account yet")
        else:
            order_status_table = PrettyTable()
            order_status_table.align = "l"
            order_status_table.title = 'Orders'
            order_status_table.field_names = [
                "Order ID",
                "Customer ID",
                "Customer full name",
                "SKU",
                "Product Name",
                "Price per unit $",
                "Ordered QTY",
                "Shipping status"
            ]
            for i in range(len(user_record['order_customer_id'])):
                order_status_table.add_row([
                    user_record['order_id'][i],
                    user_record['order_customer_id'][i],
                    user_record['order_customer_full_name'][i],
                    str(user_record['order_customer_sku'][i]),
                    str(user_record['order_customer_product_name'][i]),
                    str(user_record['order_customer_price_per_unit'][i]),
                    str(user_record['order_customer_qty'][i]),
                    user_record['order_shipping_status'][i]
                ])
            print(order_status_table)

        order_status_menu = [
            {
                'type': 'list',
                'name': 'order_status_menu-selection',
                'message': 'Update order status',
                'choices': [
                    "Yes",
                    "No"
                ],
            }
        ]

        order_status_menu_result = prompt(order_status_menu)

        if order_status_menu_result["order_status_menu-selection"] == "Yes":
            shipping_status = [
                {
                    'type': 'list',
                    'name': 'shipping_status_menu-selection',
                    'message': 'Current shipping status',
                    'choices': [
                        "Order is awaiting picking",
                        "Order is shipped",
                        "Order is delayed",
                        "order is delivered",
                        "Back to update order status"
                    ],
                }
            ]

            shipping_status_result = prompt(shipping_status)
            if shipping_status_result["shipping_status_menu-selection"] == "Order is awaiting picking":
                search_order_id = input("Please enter the order id: ")
                user_record = OrderStatus.__ecommerce_data.get(account_number)
                index = user_record["order_id"].index(search_order_id)
                user_record["order_shipping_status"][index] = "Order is awaiting picking"
                print("Order is awaiting picking")
            if shipping_status_result["shipping_status_menu-selection"] == "Order is shipped":
                search_order_id = input("Please enter the order id: ")
                user_record = OrderStatus.__ecommerce_data.get(account_number)
                index = user_record["order_id"].index(search_order_id)
                user_record["order_shipping_status"][index] = "Order is shipped"
                print("Order is shipped")
            if shipping_status_result["shipping_status_menu-selection"] == "Order is delayed":
                search_order_id = input("Please enter the order id: ")
                user_record = OrderStatus.__ecommerce_data.get(account_number)
                index = user_record["order_id"].index(search_order_id)
                user_record["order_shipping_status"][index] = "Order is delayed"
                print("Order is delayed")
            if shipping_status_result["shipping_status_menu-selection"] == "Order is delivered":
                search_order_id = input("Please enter the order id: ")
                user_record = OrderStatus.__ecommerce_data.get(account_number)
                index = user_record["order_id"].index(search_order_id)
                user_record["order_shipping_status"][index] = "Order is delivered"
                print("Order is delivered")
            if shipping_status_result["shipping_status_menu-selection"] == "Back to update order status":
                pass

        if order_status_menu_result["order_status_menu-selection"] == "No":
            pass
