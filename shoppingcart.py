from prettytable import PrettyTable

from datastorage import DataStorage


class ShoppingCart:
    """

    """
    __ecommerce_data = DataStorage.ecommerce_data  # all the data

    def __init__(self):
        self.__cart_table = PrettyTable()
        self.__seller = []
        self.__product_name = []
        self.__sku = []
        self.__price = []
        self.__pos = []
        self.__check_out_qty = []

    def add_to_cart(self, selection_id, selection_qty):
        for keys, values in ShoppingCart.__ecommerce_data.items():
            if "products" and "sku" and "prices" and "stock" in values:
                if selection_id in values["sku"]:
                    product_id = values["sku"].index(selection_id)
                    self.__seller.append(values["first_name"] + " " + values["last_name"])
                    self.__sku.append(values["sku"][product_id])
                    self.__price.append(values["prices"][product_id])
                    self.__product_name.append(values["products"][product_id])
                    self.__pos.append(product_id)
                    self.__check_out_qty.append(selection_qty)
                    self.show_cart()
                    break

    def show_cart(self):
        print("calling show cart")
        self.__cart_table.field_names = ["Seller name", "Product name", "SKU", "Price per unit $", "QTY"]
        self.__cart_table.align = "l"
        for i in range(len(self.__sku)):
            for index, data in enumerate(
                    zip(self.__seller, self.__product_name, self.__sku, self.__price, self.__check_out_qty)):
                print(data)
        print(self.__cart_table)

    def check_out(self):
        pass
