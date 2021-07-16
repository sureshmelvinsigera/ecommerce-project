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

    def __init__(self):
        self.__order_status_table = None

    def status(self, account_number=10000):
        self.__order_status_table = PrettyTable()
        self.__order_status_table.align = "l"
        self.__order_status_table.title = 'Orders'
        self.__order_status_table.field_names = [
            "Customer ID",
            "Customer full name",
            "SKU",
            "Product Name",
            "Price per unit $",
            "Ordered QTY",
            "Shipping status"
        ]

        record = OrderStatus.__ecommerce_data.get(account_number)

        if len(record['order_customer_id']) == 0:
            print("Sorry there are no orders for this account yet")
        else:
            for i in range(len(record['order_customer_id'])):
                self.__order_status_table.add_row([
                    record["order_customer_id"][i],
                    record["order_customer_full_name"][i],
                    record["order_customer_sku"][i],
                    record["order_customer_product_name"][i],
                    record["order_customer_price_per_unit"][i],
                    record["order_customer_qty"][i],
                    record["order_shipping_status"][i]
                ])
                print(self.__order_status_table)

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
                            ],
                        }
                    ]

                shipping_status_result = prompt(shipping_status)
                if shipping_status_result["shipping_status_menu-selection"] == "Order is awaiting picking":
                    print("Order is awaiting picking")
                if shipping_status_result["shipping_status_menu-selection"] == "Order is shipped":
                    print("Order is shipped")
                if shipping_status_result["shipping_status_menu-selection"] == "Order is delayed":
                    print("Order is delayed")
                if shipping_status_result["shipping_status_menu-selection"] == "Order is delivered":
                    print("Order is delivered")

            if order_status_menu_result["order_status_menu-selection"] == "No":
                pass


o = OrderStatus()
o.status()
