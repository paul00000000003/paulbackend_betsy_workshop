__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from peewee import *
# from models import BaseModel,Product
from datetime import datetime
from models import *
from make_bunch_of_records import *


def search(term):
    return Product.select().where(fn.Upper(Product.product_name).contains(fn.Upper(term)))


def list_user_products(user_id):
    return User_products.select().where(User_products.user_id == user_id).dicts()


def list_products_per_tag(tag_id):
    products = Product.select()
    representative_products = []

    for product in products:
        product_chosen = "N"
        for tag in product.tags:
            if tag.tag_id == tag_id:
                product_chosen = "Y"
        if product_chosen == "Y":
            representative_products.append(product.product_name)
    return representative_products


def add_product_tags(product_, tag_names):
    if isinstance(tag_names, list):
        for tag_name in tag_names:
            if Tags.select().where(Tags.name == tag_name):
                tag = Tags.get(Tags.name == tag_name)
            else:
                Tags.create(name=tag_name)
                tag = Tags.get(Tags.name == tag_name)
            if tag in product_.tags:
                None
            else:
                product_.tags.add(tag)


def add_product_to_catalog(user_id, product):
    #   Een produkt dat al in de database aanwezig was, was al aan een catalogus
    #   gekoppeld. Ik begreep dus niet hoe je op basis van een bestaand produkt een record aan de catalogus
    #   toe gaat voegen.
    if product["product_name"] != None and product["price_per_unit"] != None and user_id != 0:
        if Catalog.select().where(Catalog.user_id == user_id):
            None
        else:
            Catalog.create(user_id=user_id)
        catalog_id = Catalog.get(user_id == user_id).catalog_id
        if Product.select().where(Product.product_name == product['product_name']):
            product_ = Product.get(
                Product.product_name == product['product_name'])
            add_product_tags(product_, product['tag_names'])
        else:
            Product.create(product_name=product["product_name"],
                           description=product["description"],
                           price_per_unit=product["price_per_unit"],
                           number_in_stock=product["number_in_stock"],
                           catalog_id=catalog_id,
                           tags=[])
            product_ = Product.get(
                Product.product_name == product["product_name"])
            add_product_tags(product_, product['tag_names'])
    else:
        print("Product requirements are not met of user_id doesn't have a proper value")


def update_stock(product_name, new_quantity):
    product = Product.get(Product.product_name == product_name)
    product.number_in_stock = new_quantity
    product.save()

# error in assignment : price misses in transaction model


def purchase_product(product_id, buyer_id, quantity, price):
    TransactionData.create(user_id=buyer_id, product_id=product_id,
                           number=quantity, sell_date=datetime.now(), sell_price=price)


def remove_product(product_name):
    product = Product.get(Product.product_name == product_name)
    product.delete_instance()


create_tables()

"""
I left the statements underneath which I used solely for testing purposes. Be aware the datamodel is based on the DecimalFormat on
prices as well as contraints on Primary and Foreign keys. Other than that a few fields have other specific contraints such a positive number
"""
make_bunch_of_records()
chosen_products = search("Trui")
for product in chosen_products:
    print("product "+product.product_name)

query = list_user_products(1)

for regel in query:
    print("list_user_products "+regel.__repr__())

query = list_products_per_tag(1)
print("en nu de producten met tag name Domestic")
for regel in query:
    print(regel)

product = {"product_name": "pears",
           "description": "Spanish delicious pears",
           "price_per_unit": 0.6546,
           "number_in_stock": 65,
           "tag_names": ["Domestic", "Food", "Kitchen"]}

add_product_to_catalog(1, product)
# eigenlijk is het beter om nog een validatie op het user_id te zetten, maar je kunt er over redetwisten of je dat in de bovenstaande functie wilt doen


update_stock("koltrui", 25)

purchase_product(1, 1, 1, 90.1234)

# Be aware of enforced primary-key, foreign-key relationships when removing a product
remove_product("appels")
