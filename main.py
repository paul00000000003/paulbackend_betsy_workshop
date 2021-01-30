__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from peewee import *
#from models import BaseModel,Product
from datetime import datetime
from models import *
from make_bunch_of_records import *


def search(term):
    return Product.select().where(fn.Upper(Product.product_name).contains(fn.Upper(term)))


def list_user_products(user_id):
    return User_products.select().where(User_products.user_id == user_id).dicts()


def list_products_per_tag(tag_id):
    return Product.select().where(Product.color == tag_id or Product.product_category == tag_id or Product.appliance_place == tag_id).dicts()
    # hmmmm : was dit wel de bedoeling ? Dus een tag_id is uniek voor alle soorten tags per produkt ?


def add_product_to_catalog(user_id, product_name):
    # a user catalog ? WTF is a user catalog ?
    Catalog.create(user_id=user_id, product_name=product_name)


def update_stock(product_name, new_quantity):
    product = Product.get(Product.product_name == product_name)
    product.number_in_stock = new_quantity
    product.save()


# error in assignment : price misses in transaction model
def purchase_product(product_name, buyer_id, quantity, price):
    TransactionData.create(user_id=buyer_id, product_name=product_name,
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
query = list_user_products(1)

for regel in query:
    print(regel)
for product in chosen_products:
    print("geselecteerd produkt : "+product.product_name)
query = list_products_per_tag("blue")
print("en nu de blauwe")
for regel in query:
    print(regel)
add_product_to_catalog(1, "koltrui")
update_stock("koltrui", 25)
purchase_product("koltrui", 1, 1, 90.1234)

# I kidded myself trying to remove a record from the table Product whereas it was still present in other tables. Be aware this is not possible due
# to primary_key foreign-key contraints. 
remove_product("appels")
# Be aware prices are rounded automatically due to the definition of the price format both in the product and transaction data table. 
purchase_product("oranges", 1, 1, 0.8912)
"""
