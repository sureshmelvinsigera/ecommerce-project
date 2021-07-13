from datastorage import DataStorage


class Order:
    """

    """
    __ecommerce_data = DataStorage.ecommerce_data  # all the data

    def __init__(self, customer_record, customer_address, customer_cc, seller_id, sku, pos, check_out_qty):
        self.__record = None
        self.process_order(customer_record, customer_address, customer_cc, seller_id, sku, pos, check_out_qty)

    def process_order(self, customer_record, customer_address, customer_cc, seller_id, sku, pos, check_out_qty):
        # look up seller by id
        for i in range(len(seller_id)):
            # retrieve the seller record
            self.__record = Order.__ecommerce_data.get(seller_id[i])
            # for each sku in the customer cart check if it's a match with the seller sku data list
            for r in range(len(self.__record["sku"])):
                if sku[i] == self.__record["sku"][r]:
                    print("Before ", Order.__ecommerce_data.get(seller_id[i])["stock"][r])
                    # update the new stock qty for each seller
                    Order.__ecommerce_data.get(seller_id[i])["stock"][r] = \
                        Order.__ecommerce_data.get(seller_id[i])["stock"][r] - check_out_qty[i]
                    print("After ", Order.__ecommerce_data.get(seller_id[i])["stock"][r])
        del self
