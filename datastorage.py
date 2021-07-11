class DataStorage:
    """

    """
    ecommerce_data = {
        10000: {
            "store_name": "the book club",
            'first_name': 'suresh',
            'last_name': 'sigera',
            'email': 'sms@xyz.com',
            'password': 'UDwh&AWD72g21',
            'sku': ['sk1001', 'sk1002', 'sk1003'],
            'products': ['Python Crash Course, 2nd Edition', 'Automate The Boring Stuff With Python, 2nd Edition',
                         'Learning Python, 5th Edition'],
            'prices': [29.99, 33.99, 33.86],
            'stock': [10, 12, 12],
            'type': 'owner',
        },
        10001:
            {
                "store_name": "chris's culinary store",
                'first_name': 'chris',
                'last_name': 'herzog',
                'email': 'chriher22@aol.com',
                'password': 'UDwh&AWD72g22',
                'sku': ['sk1004', 'sk1004', 'sk1006'],
                'products': ['Calphalon Classic Oil-Infused Ceramic PTFE and PFOA Free Cookware',
                             'Silicone Cooking Utensil Set',
                             'Flour Water Salt Yeast: The Fundamentals of Artisan Bread and Pizza'],
                'prices': [299.99, 21.99, 17.99],
                'stock': [100, 112, 23],
                'type': 'seller',
                'orders': {
                    1001: {

                    }
                }
            },
        10002:
            {
                "store_name": "joseph's cooking and baking",
                'first_name': 'joseph',
                'last_name': 'smith',
                'email': 'JosephSSmith@rhyta.com',
                'password': 'UDwh&AWD72g23',
                'sku': ['sk1007', 'sk1008', 'sk1009'],
                'products': ['Ball Complete Book of Home Preserving',
                             'Stainless Steel Mixing Bowl Set',
                             'PAM Cooking Spray Butter Flavor, 5 Oz'],
                'prices': [19.99, 24.99, 5.99],
                'type': 'seller'
            },
        10003:
            {
                'first_name': 'j',
                'last_name': 'Smith',
                'email': 'jj@rhyta.com',
                'password': 'UDwh&AWD72g23',
                'products': ['B1', 'B2', 'B3'],
                'prices': [1.99, 2.99, 3.99],
                'type': 'customer'
            },
    }
