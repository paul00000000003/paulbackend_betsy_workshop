__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

# from models import BaseModel,Product
from datetime import datetime
from models import *
from make_bunch_of_records import *


def search(term):
    return Product.select().where(fn.Upper(Product.product_name).contains(fn.Upper(term)))


def list_user_products(user_id):
    # to collect these three fields it's necessary to combine three tables. The switch is also necessary
    return User_product.select(User.name, Product.product_name, User_product.number).join(
        Product).switch(User_product).join(
        User).where(User_product.user_id == user_id)


def list_products_per_tag(tag_id):
    #   Since this is a manytomany relationship i don't think a join is possible
    #   That's why I think this is the easiest way to program this
    ProductTag.select(Product.product_name, Tag.name).join(Product).switch(
        ProductTag).join(Tag)


"""
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
"""


def update_product_in_user_catalog(user_id, product_name, new_quantity):
    #   Just to be on the safe side a check on the table Product and user are carried out
    #   before adding the product to user_products.
    product_id = 0
    if Product.select().where(Product.product_name == product_name):
        product_id = Product.get(Product.product_name == product_name)
        product_exists = True
    else:
        product_exists = False
    if User.select().where(User.user_id == user_id):
        user_exists = True
    else:
        user_exists = False
    if product_exists == True and user_exists == True:
        if User_product.select().where(User_product.product_id == product_id and User_product.user_id == user_id):
            user_product = User_product.get(
                User_product.product_id == product_id and User_product.user_id == user_id)
            user_product.number = new_quantity
            user_product.save()
        else:
            User_product.create(product_id=product_id,
                                user_id=user_id,
                                number=new_quantity)


def purchase_product(product_id, buyer_id, quantity, price):
    Transaction.create(user_id=buyer_id, product_id=product_id,
                       number=quantity, sell_date=datetime.now(), sell_price=price)


def remove_product(product_name):
    product = Product.get(Product.product_name == product_name)
    product.delete_instance()


def remove_product_from_user_catalog(product_name, user_id):
    if User_product.select().where(User_product.user_id == user_id and User_product.product_name == product_name):
        user_product = User_product.get(
            User_product.product_name == product_name)
        user_product.delete_instance()


create_tables()
"""
normally we wouldn't use this function in this script due to the fact it's normally created elsewhere
However for the sake of this script it's ok since we also want to create the database once. Tables are only
created if they dont't yet exist.

I left the statements underneath which I used solely for testing purposes. Be aware the datamodel is based on the DecimalFormat on
prices as well as contraints on Primary and Foreign keys. Other than that a few fields have other specific contraints such a positive number
"""
make_bunch_of_records()
chosen_products = search("Trui")
for product in chosen_products:
    print("product "+product.product_name)

query = list_user_products(1)

for regel in query.dicts():
    print("list_user_products "+regel.__repr__())

query = list_products_per_tag(1)
print("en nu de producten met tag name Domestic")
print(query)

update_product_in_user_catalog(1, "Trui", 25)

purchase_product(1, 1, 1, 90.1234)

remove_product("appels")
