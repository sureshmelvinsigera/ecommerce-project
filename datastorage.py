__author__ = "Suresh Melvin Sigera"
__copyright__ = "Copyright 2021, The ESSEX Project"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Suresh Melvin Sigera"
__email__ = "sureshsigera@gmail.com"
__status__ = "Staging"


class DataStorage:
    """
    This class provides initial dataset to mimic ecommerce application.
    According to this data structure, there are three different type of users: site owner, seller and customer.
    This class does not contain any methods, it contains a single class variable to hold the entire dataset.
    """

    ecommerce_data = {
        10000: {
            'first_name': 'suresh',
            'last_name': 'sigera',
            'email': 'sms@xyz.com',
            'password': 'UDwh&AWD72g21',
            'sku': ['su1001', 'su1002', 'su1003'],
            'products': ['Python Crash Course, 2nd Edition',
                         'Automate The Boring Stuff With Python, 2nd Edition',
                         'Learning Python, 5th Edition'],
            'prices': [29.99, 33.99, 33.86],
            'stock': [10, 12, 12],
            'type': 'owner',
        },
        10001:
            {
                'first_name': 'chris',
                'last_name': 'herzog',
                'email': 'chriher22@aol.com',
                'password': 'UDwh&AWD72g22',
                'sku': ['ch1004', 'ch1005', 'ch1006'],
                'products': [
                    'Calphalon Classic Oil-Infused Ceramic PTFE and PFOA Free Cookware',
                    'Silicone Cooking Utensil Set',
                    'Flour Water Salt Yeast: The Fundamentals of Artisan Bread and Pizza'
                ],
                'prices': [299.99, 21.99, 17.99],
                'stock': [100, 112, 23],
                'type': 'seller',
            },
        10002:
            {
                'first_name': 'joseph',
                'last_name': 'smith',
                'email': 'JosephSSmith@rhyta.com',
                'password': 'UDwh&AWD72g23',
                'sku': ['jo1007', 'jo1008', 'jo1009'],
                'products': [
                    'Ball Complete Book of Home Preserving',
                    'Stainless Steel Mixing Bowl Set',
                    'PAM Cooking Spray Butter Flavor, 5 Oz'
                ],
                'prices': [19.99, 24.99, 5.99],
                'stock': [10, 100, 0],
                'type': 'seller',
                'orders': [[], [], [], []],  # sku, qty, customer_id, shipping_status
            },
        10003:
            {
                'first_name': 'j',
                'last_name': 'Smith',
                'email': 'jj@rhyta.com',
                'password': 'UDwh&AWD72g23',
                'type': 'customer'
            },
    }
