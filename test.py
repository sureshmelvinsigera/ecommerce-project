from prettytable import PrettyTable

products = ["test", "test", "test"]
sku = ["test", "test", "test"]
price = [1.99, 2.99, 3.00]
data = zip(products, sku, price)

for prod, sku, price in zip(products, sku, price):
    print('{} {} {}'.format(prod, sku, price))
