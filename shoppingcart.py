from prettytable import PrettyTable

from datastorage import DataStorage
from order import Order


class ShoppingCart:
    """

    """
    __ecommerce_data = DataStorage.ecommerce_data  # all the data

    def __init__(self):
        self.__seller_id = []
        self.__cart_table = None
        self.__seller = []
        self.__product_name = []
        self.__sku = []
        self.__price = []
        self.__pos = []
        self.__check_out_qty = []
        self.__order = None
        self.__cart_total_table = None
        self.__total = 0

    def add_to_cart(self, selection_id, selection_qty):
        """
        add user product selection to the cart instance variables
        """
        # read the data from data storage
        for keys, values in ShoppingCart.__ecommerce_data.items():
            # check if the product contain necessary data before proceed
            if "products" and "sku" and "prices" and "stock" in values:
                # check if it is a correct sku code from the data storage
                if selection_id in values["sku"]:
                    # add product information to the instance variables
                    self.__seller_id.append(keys)
                    product_id = values["sku"].index(selection_id)
                    self.__seller.append(values["first_name"] + " " + values["last_name"])
                    self.__sku.append(values["sku"][product_id])
                    self.__price.append(values["prices"][product_id])
                    self.__product_name.append(values["products"][product_id])
                    self.__pos.append(product_id)
                    self.__check_out_qty.append(selection_qty)

    def show_cart(self):
        """
        Show up to date shopping cart when user select the menu
        """
        # create new instance of the shopping cart
        self.__cart_table = PrettyTable()
        self.__cart_table.field_names = ["Seller name", "Product name", "SKU", "Price per unit $", "QTY"]
        self.__cart_table.align = "l"
        total = 0
        # zip and loop over each product
        for seller, product_name, sku, price_per_unit, qty in zip(
                self.__seller, self.__product_name, self.__sku,
                self.__price, self.__check_out_qty):
            # add product information to the cart table for later uses
            self.__cart_table.add_row(
                [seller, product_name, sku,
                 str(price_per_unit) + " * " + str(qty) + " = " + str(price_per_unit * qty),
                 qty])
            # calculate the total cost for all the items in the shopping cart
            total += price_per_unit * qty
        # print the current cart content
        print(self.__cart_table)
        cart_total_table = PrettyTable()
        # generate the total
        cart_total_table.field_names = ["Cart total $"]
        cart_total_table.add_row([total])
        print(cart_total_table)

    def check_out(self, account_number):
        """
        this method will create a new order based on the items user has added to the shopping cart
        """
        # obtain the current logged in users account number
        customer_record = ShoppingCart.__ecommerce_data.get(account_number)
        customer_address = "112 main street"
        customer_cc = "credit card information"
        # crate a new order instance
        new_order_request = Order()
        # call the order process method
        new_order_request.process_order(
            customer_record,
            customer_address, customer_cc, self.__seller_id, self.__sku,
            self.__pos,
            self.__check_out_qty
        )
        # the order is successful, remove all items from the cart by emptying the instance variables
        if new_order_request.status == "Success":
            self.__seller_id = []
            self.__cart_table = None
            self.__seller = []
            self.__product_name = []
            self.__sku = []
            self.__price = []
            self.__pos = []
            self.__check_out_qty = []
            self.__order = None
            self.__cart_total_table = None
            self.__total = 0
