from PyInquirer import prompt, Token
from prettytable import PrettyTable
from prompt_toolkit.styles import style_from_dict
from datastorage import DataStorage


class Product:
    """

    """
    __ecommerce_data = DataStorage.ecommerce_data  # all the data

    def __init__(self):
        self.__products_table = PrettyTable()
        self.__sellers_table = None
        self.__customers_table = None

    @staticmethod
    def add_product(account_number):
        """
        this method asks the user the enter the product name, price, qty and save the information to the
        ecommerce_data dictionary.
        :return:
        """
        print(30 * "-", "add new product", 30 * "-")
        # product_name = input("Please enter the product name: ")
        # product_price = float(input("Please enter the product price: "))
        # product_stock_qty = int(input("Please enter the stock qty: "))
        # # append product attributes to the list
        # ecommerce_data.get(account_number)["products"].append(product_name)
        # ecommerce_data.get(account_number)["prices"].append(product_price)
        # ecommerce_data.get(account_number)["stock"].append(product_stock_qty)

        # generate unique sku for the new product based on the last product in the dictionary

        for key, values in Product.__ecommerce_data.items():
            for k, v in values.items():
                print(k, v)

        # sku_pos = len(ecommerce_data.get(account_number)["sku"]) - 1
        # sku = ecommerce_data.get(account_number)["sku"][sku_pos]
        # # separate text from integer
        # temp_sku = re.compile("([a-zA-Z]+)([0-9]+)")
        # res = temp_sku.match(sku).groups()
        # sku_str = "sk" + str(int(res[1]) + 1)
        # ecommerce_data.get(account_number)["sku"].append(sku_str)
        # print("product has been successfully added")

    @staticmethod
    def update_product(account_number):
        """
        update product information using product id and account_number
        """
        print(30 * "-", "Update product", 30 * "-")

        style = style_from_dict({
            Token.Separator: '#cc5454',
            Token.QuestionMark: '#673ab7 bold',
            Token.Selected: '#cc5454',  # default
            Token.Pointer: '#673ab7 bold',
            Token.Instruction: '',  # default
            Token.Answer: '#f44336 bold',
            Token.Question: '',
        })

        product_edit_menu = [
            {
                'type': 'list',
                'name': 'product-edit-menu-selection',
                'message': 'Edit product information',
                'choices': Product.__ecommerce_data.get(account_number)["products"],
            }
        ]

        product_edit_menu_result = prompt(product_edit_menu, style=style)

        # print all the products that belongs to the seller
        for i in range(len(Product.__ecommerce_data.get(account_number)["products"])):
            if product_edit_menu_result['product-edit-menu-selection'] == \
                    Product.__ecommerce_data.get(account_number)["products"][i]:
                print(f"Editing ... {Product.__ecommerce_data.get(account_number)['products'][i]}")
                # edit product related fields
                product_name = input("Please enter the new product name: ")
                product_price = float(input("Please enter the new product price: "))
                product_stock_qty = int(input("Please enter the new stock qty: "))
                # save data back to the dictionary
                Product.__ecommerce_data.get(account_number)["products"][i] = product_name
                Product.__ecommerce_data.get(account_number)["prices"][i] = product_price
                Product.__ecommerce_data.get(account_number)["stock"][i] = product_stock_qty
        print("product has been successfully updated")

    @staticmethod
    def delete_product(account_number):
        """
        delete product that belongs to the seller
        """
        # load all the products from the current seller
        choices = Product.__ecommerce_data.get(account_number)["products"]
        # if there is no products exists then show the custom error message
        if len(choices) == 0:
            choices.append("No products found in this seller shop")

        product_delete_menu = [
            {
                'type': 'list',
                'name': 'product-delete-menu-selection',
                'message': 'Delete product',
                'choices': choices,
            }
        ]
        product_delete_menu_result = prompt(product_delete_menu)

        # delete product belongs to current seller
        Product.__ecommerce_data.get(account_number)["products"].pop(
            Product.__ecommerce_data.get(account_number)["products"].index(
                product_delete_menu_result['product-delete-menu-selection']))
        print("Record has been successfully deleted")

    def show_all_products(self, account_number=None):
        """
        show all the products belongs to the site owner, seller and logged in user
        """
        # if the current user is customer then show all the products
        if account_number is None:
            self.__products_table.title = 'Products from all stores'
            self.__products_table.field_names = ["Selection id", "Seller name",
                                                 "SKU", "Product name", "Price per unit $",
                                                 "In stock QTY"]
            self.__products_table.align = "l"
            set_index = 0
            for keys, values in Product.__ecommerce_data.items():
                if "products" and "sku" and "prices" and "stock" in values:
                    # logic to loop over sku, products, prices, and stock
                    for index, data in enumerate(
                            zip(values["sku"], values["products"], values["prices"], values["stock"])):
                        set_index += 1
                        # generate the table
                        self.__products_table.add_row([
                            set_index, keys,
                            values["sku"][index],
                            values["products"][index],
                            values["prices"][index],
                            values["stock"][index]
                        ])
            print(self.__products_table)

        else:
            # if the current user is seller or site owner
            self.__products_table.title = 'Your product list'
            record = Product.__ecommerce_data.get(account_number)
            self.__products_table.field_names = ["SKU", "Product name", "Price per unit $", "In stock QTY"]
            self.__products_table.align = "l"
            for i in range(len(record['products'])):
                self.__products_table.add_row(
                    [record['sku'][i], record['products'][i], record['prices'][i], record['stock'][i]])
            print(self.__products_table)
