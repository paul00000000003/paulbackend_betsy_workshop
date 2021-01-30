from peewee import *
from models import *

database = SqliteDatabase('betsy_workshop.db')


def make_bunch_of_records():
    """
    De toegepaste contraints zijn :
    Je moet eerst een User en een Product opzetten voordat je
    een record in Catalog,TransactionData,User_products kunt zetten. Dit gaat gepaard
    met het definieren van een primary key in Product en User en foreign_keys in Catalog,TransactionData en User_products
    """

    if Product.select().where(Product.product_name == "koltrui"):
        None
    else:
        Product.create(product_name="koltrui",
                       description="trui met hoge kol",
                       price_per_unit=89.7634,
                       number_in_stock=20, color="blue",
                       product_category="clothes",
                       appliance_place="domestic")
    if Product.select().where(Product.product_name == "koltrui met revers"):
        None
    else:
        Product.create(product_name="koltrui met revers",
                       description="trui met revers",
                       price_per_unit=0.3412,
                       number_in_stock=18,
                       color="blue",
                       product_category="clothes",
                       appliance_place="domestic")
    if Product.select().where(Product.product_name == "appels"):
        None
    else:
        Product.create(product_name="appels",
                       description="lekkere Spaanse appels",
                       price_per_unit=2.4564,
                       number_in_stock=18,
                       color="red",
                       product_category="food",
                       appliance_place="domestic")
    if User.select().where(User.user_id == 1):
        None
    else:
        User.create(user_id=1, name="Paul van Mierlo",
                    street="Roemer Visscherstraat 35", town="Leiden")
    if User.select().where(User.user_id == 2):
        None
    else:
        User.create(user_id=2, name="Mariza Dacoron",
                    street="Roemer Visscherstraat 35", town="Leiden")

    if User.select().where(User.user_id == 3):
        None
    else:
        User.create(user_id=3, name="Pete Petterson",
                    street="43 Bloomingdale lane", town="Bloomingdale")

    if User.select().where(User.user_id == 4):
        None
    else:
        User.create(user_id=4, name="Jack Nicholson",
                    street="43 Park Avenue", town="Bloomsdale")

    if User_products.select().where(User_products.user_id == 1):
        None
    else:
        User_products.create(user_id=1, product_name="koltrui", number=2)
        User_products.create(
            user_id=1, product_name="koltrui met revers", number=2)

    if User_products.select().where(User_products.user_id == 2):
        None
    else:
        User_products.create(user_id=2, product_name="koltrui", number=2)
        User_products.create(
            user_id=2, product_name="koltrui met revers", number=3)

    if Product.select().where(Product.product_name == "oranges"):
        None
    else:
        Product.create(product_name="oranges", description="Very good tasting Marocan oranges", price_per_unit=0.987,
                       color="orange", product_category="food", appliance_place="random", number_in_stock=250)

    if User_products.select().where(User_products.user_id == 4 and User_products.product_name == "orange"):
        None
    else:
        User_products.create(user_id=4, product_name="oranges", number=10)
