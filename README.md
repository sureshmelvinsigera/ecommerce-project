

# ECommerce System Implementation

The system comprises 14 different classes:

#### datastorage class
This class provides an initial dataset to facilitate all the CRUD operations throughout the entire program. All the Python classes in this system software use this data set to store and retrieve data during the runtime. According to this data structure, there are three different users: site owner, seller and customer. This class does not contain any methods. It incorporates a single class variable to hold the entire dataset.

#### admin class
This class provides utility methods for admin-related tasks, such as displaying all the shoppers, and all the sellers to the website owner. It also generates the admin user interface.

#### customer class
This class provides utility methods for customer-related tasks, such as product search, adding a product to the shopping cart, displaying the shopping cart for the logged-in user, product checkout and log out functionality. It also generates the customer user interface.

#### seller class
This class provides utility methods to generate the seller user interface. It also contains seller related functionality, such as product search, which shows all the products that belong to the currently logged-in sellers. The seller can also add new products, update and delete existing products, and check pending orders from different customers. 

#### order class
This class provides utility methods order related tasks. The primary responsibility of this class is to obtain all the required user information from the application UI and transfer it to the data access layer.

This class is also liable for monitoring the following bases-cases:

 - The purchaser might try to check out an empty cart.
 - The purchaser adds one or more products to the shopping cart and proceeded to the 
 order page, but then add another product. The system must maintain the state by 
 accessing the data layer.
 - Several buyers might endeavour to buy the same product, if so data access layer must 
 update the presentation layer.
 - The user successfully executed all the required steps to complete the order. At this stage, the data access layer must have the latest data from the local storage and pass it down to the business layer. If the user visits the checkout page, it should be empty.
 - Simultaneously, when the order is successfully handled by the system, the order class is also responsible for generating a six digit ASCII code which considered being the order number.
 - Once the unique order number is created, the business logic will update the sellers account to show the pending orders. 

```python
...
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
                            while order_id not in Order.__ecommerce_data.get(seller_id[i])["order_id"]:
                                Order.__ecommerce_data.get(seller_id[i])["order_id"].append(order_id)
                            Order.__ecommerce_data.get(seller_id[i])["order_customer_full_name"].append(
                                customer_record["first_name"] + " " + customer_record["last_name"])
                            Order.__ecommerce_data.get(seller_id[i])["order_customer_id"].append(account_number)
                            Order.__ecommerce_data.get(seller_id[i])["order_customer_product_name"].append(
                                check_out_product_name)
                            Order.__ecommerce_data.get(seller_id[i])["order_customer_sku"].append(str(check_out_sku)[1:-1])
                            Order.__ecommerce_data.get(seller_id[i])["order_customer_qty"].append(
                                str(check_out_qty)[1:-1])
                            Order.__ecommerce_data.get(seller_id[i])["order_shipping_status"].append(
                                "Order is awaiting picking")
                            # Order.__ecommerce_data.get(seller_id[i])["order_customer_total"].append(
                            #     check_out_qty * check_out_price)
                            Order.__ecommerce_data.get(seller_id[i])["order_customer_price_per_unit"].append(
                                check_out_price)

                print("Your order has been successfully processed")
...

```

#### orderstatus class

This class provides the site admin or the 3rd party seller to revise the shipping status. Such that, Order is awaiting picking, Order is shipped, Order is delayed, or Order is delivered by using the six digits unique order number which was generated by the order class.

