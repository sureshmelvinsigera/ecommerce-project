from prettytable import PrettyTable

from datastorage import DataStorage


class ProductSearch:
    """
    """
    __ecommerce_data = DataStorage.ecommerce_data  # all the data

    def __init__(self):
        """
        """
        self.__search_results_table = PrettyTable()
        self.__seller = []
        self.__product_name = []
        self.__sku = []
        self.__price = []
        self.__result = []

    def search_products(self, keyword):
        """

        """
        for keys, values in ProductSearch.__ecommerce_data.items():
            # check if the product contain necessary data before proceed
            if "products" and "sku" and "prices" and "stock" in values:
                for index, product in enumerate(
                        zip(values["sku"], values["products"],
                            values["stock"])):
                    # prints
                    if keyword in product[1]:
                        print(values)
                        self.__result.append(product)
                        # print("found")
                    # if keyword in product:
                    #     print(index, product)
                    # self.__seller.append(str(values["first_name"] + " " + values["last_name"]))
                    # self.__sku.append(values["sku"])
                    # print(self.__sku)
                    # self.__seller.append(product)
        if len(self.__result) == 0:
            print(f"No search results for the keyword {keyword}")
        else:
            print(self.__result)


p = ProductSearch()
p.search_products("Stainless")
