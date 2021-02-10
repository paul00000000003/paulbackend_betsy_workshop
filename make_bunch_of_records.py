from peewee import *
from models import *

database = SqliteDatabase('betsy_workshop.db')


def add_tag(product, tag_name):
    tag = Tag.get(Tag.name == tag_name)
    if tag in product.tags:
        None
    else:
        product.tags.add([tag])


def make_bunch_of_records():
    if User.select().where(User.name == "Paul van Mierlo"):
        None
    else:
        User.create(name="Paul van Mierlo",
                    street="Roemer Visscherstraat 35", town="Leiden")
    if Tag.select().where(Tag.name == "Domestic"):
        None
    else:
        Tag.create(name="Domestic")

    if Tag.select().where(Tag.name == "Tool"):
        None
    else:
        Tag.create(name="Tool")

    if Tag.select().where(Tag.name == "Garden"):
        None
    else:
        Tag.create(name="Garden")

    if Tag.select().where(Tag.name == "Clothes"):
        None
    else:
        Tag.create(name="Clothes")

    if Tag.select().where(Tag.name == "WardRobe"):
        None
    else:
        Tag.create(name="WardRobe")

    if Product.select().where(Product.product_name == "koltrui"):
        None
    else:
        Product.create(product_name="koltrui",
                       description="trui met hoge kol",
                       price_per_unit=89.7634,
                       tags=[],
                       catalog_id=1)
    koltrui = Product.get(Product.product_name == "koltrui")
    add_tag(koltrui, "Domestic")
    add_tag(koltrui, "WardRobe")
    if Product.select().where(Product.product_name == "koltrui met revers"):
        None
    else:
        Product.create(product_name="koltrui met revers",
                       description="trui met revers",
                       price_per_unit=0.3412,
                       tags=[],
                       catalog_id=1)
    if Product.select().where(Product.product_name == "appels"):
        None
    else:
        Product.create(product_name="appels",
                       description="lekkere Spaanse appels",
                       price_per_unit=2.4564,
                       tags=[],
                       catalog_id=1)
    if User.select().where(User.name == "Paul van Mierlo"):
        None
    else:
        User.create(name="Paul van Mierlo",
                    street="Roemer Visscherstraat 35", town="Leiden")
    if User.select().where(User.name == "Mariza Dacoron"):
        None
    else:
        User.create(name="Mariza Dacoron",
                    street="Roemer Visscherstraat 35", town="Leiden")

    if User.select().where(User.name == "Pete Petterson"):
        None
    else:
        User.create(name="Pete Petterson",
                    street="43 Bloomingdale lane", town="Bloomingdale")

    if User.select().where(User.name == "Jake Nicholson"):
        None
    else:
        User.create(name="Jack Nicholson",
                    street="43 Park Avenue", town="Bloomsdale")

    if User_product.select().where(User_product.user_id == 1):
        None
    else:
        User_product.create(user_id=1, product_id=1, number=2)
        User_product.create(user_id=1, product_id=2, number=2)

    if User_product.select().where(User_product.user_id == 2):
        None
    else:
        User_product.create(user_id=2, product_id=1, number=2)
        User_product.create(
            user_id=2, product_id=2, number=3)

    if Product.select().where(Product.product_name == "oranges"):
        None
    else:
        Product.create(product_name="oranges", description="Very good tasting Marocan oranges", price_per_unit=0.987,
                       number_in_stock=250, tags=[], catalog_id=1)

    oranges_id = Product.get(Product.product_name == "oranges")

    if User_product.select().where(User_product.user_id == 4 and User_product.product_id == oranges_id):
        None
    else:
        User_product.create(user_id=4, product_id=oranges_id, number=10)
