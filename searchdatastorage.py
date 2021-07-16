__author__ = "Suresh Melvin Sigera"
__copyright__ = "Copyright 2021, The ESSEX Project"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Suresh Melvin Sigera"
__email__ = "sureshsigera@gmail.com"
__status__ = "Staging"

# import required dependencies
from prettytable import PrettyTable

from datastorage import DataStorage


class ProductSearch:
    """
    This class provides utility methods to search products in the database by given keyword.
    """
    # load local data storage
    __ecommerce_data = DataStorage.ecommerce_data

    def __init__(self):
        self.__search_results_table = None
        self.__result_product_name = []
        self.__result_sku = []
        self.__result_stock = []
        self.__result_price = []

    def search_products(self, keyword):
        """
        If the results are available upon request, this method will generate a table
        or else show messaged to the user
        :param keyword:
        :return:
        """
        # loop over all the keys in the data storage
        for keys, values in ProductSearch.__ecommerce_data.items():
            # find where key, pair values that represent seller or store owner
            if "products" and "sku" and "prices" and "stock" in values:
                # loop over each product in the list
                for i in range(len(values["products"])):
                    # convert existing data to lower case and the search keyword to lower case
                    if keyword.lower() in values["products"][i].lower():
                        # append the search result
                        self.__result_sku.append(values["sku"][i])
                        self.__result_product_name.append(values["products"][i])
                        self.__result_stock.append(values["stock"][i])
                        self.__result_price.append(values["prices"][i])
        # base-case, no search results found for the keyword
        if len(self.__result_sku) == 0:
            print(f"No search results for the keyword {keyword}")
        else:
            # crate instance of the PrettyTable() to generate results
            self.__search_results_table = PrettyTable()
            self.__search_results_table.align = "l"
            self.__search_results_table.field_names = ["SKU", "Product name", "QTY", "Price per unit $"]
            # loop over the search results
            for i in range(len(self.__result_sku)):
                # add each result to PrettyTable() instance
                self.__search_results_table.add_row(
                    [self.__result_sku[i], self.__result_product_name[i], self.__result_stock[i],
                     self.__result_price[i]])
            print(self.__search_results_table)

p = ProductSearch()
p.search_products("Python")
