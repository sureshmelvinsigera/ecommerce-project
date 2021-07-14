from PyInquirer import prompt

from datastorage import DataStorage


class Order:
    """

    """
    __ecommerce_data = DataStorage.ecommerce_data  # all the data
    status = None

    @staticmethod
    def process_order(customer_record, customer_address, customer_cc, seller_id, sku, pos, check_out_qty):

        order_menu = [
            {
                'type': 'list',
                'name': 'order_menu-selection',
                'message': 'Would you like to proceed ?',
                'choices': [
                    'Yes', 'No'
                ]
            }
        ]

        order_menu_selection = prompt(order_menu)
        if order_menu_selection['order_menu-selection'] == 'Yes':
            if len(sku) == 0:
                # if the user decided to check out an empty shopping cart, then handle that use case
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
                        if sku[i] == record["sku"][r]:
                            # for debug purpose only
                            # print("Before ", Order.__ecommerce_data.get(seller_id[i])["stock"][r])
                            # update the new stock qty for each seller
                            Order.__ecommerce_data.get(seller_id[i])["stock"][r] = \
                                Order.__ecommerce_data.get(seller_id[i])["stock"][r] - check_out_qty[i]
                            # for debug purpose only
                            # print("After ", Order.__ecommerce_data.get(seller_id[i])["stock"][r])
                print("Your order has been successfully processed")
                # update the state, so the shopping cart class is aware of it
                Order.status = "Success"
        if order_menu_selection['order_menu-selection'] == 'No':
            # update the state, so the shopping cart class is aware of it
            Order.status = "No"
        # return the order status for later use
        return Order.status
