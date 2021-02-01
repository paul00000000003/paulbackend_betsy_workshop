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


def add_product_to_catalog(user_id, product_id):
    #   Een produkt dat al in de database aanwezig was, was al aan een catalogus
    #   gekoppeld. Ik begreep dus niet hoe je op basis van een bestaand produkt een record aan de catalogus
    #   toe gaat voegen. Er is door Donatas een database opzet gecreeerd die ik in twijfel trek.
    if Product.select().where(Product.product_id == product_id):
        if Catalog.select().where(Catalog.user_id == user_id):
            catalog = Catalog.get(Catalog.user_id == user_id)
            id = catalog.catalog_id
        else:
            id = 1
            Catalog.create(catalog_id=1, user_id=user_id)
        Catalog.create(user_id=user_id, product_id=product_id)
        product = Product.get(Product.product_id == product_id)
        product.catalog_id = id
        product.save()
    else:
        print("This function doesn't work if the product doesn't exist yet. Of course it \n would be possible to defined the product first and \n then add it to the catalog but this involves more fields")


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

add_product_to_catalog(1, 1)

update_stock("koltrui", 25)

purchase_product(1, 1, 1, 90.1234)

# Be aware of enforced primary-key, foreign-key relationships when removing a product
remove_product("appels")
"""
