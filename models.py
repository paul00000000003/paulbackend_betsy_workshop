# Models go here

from peewee import Model, SqliteDatabase, IntegerField, AutoField, DateField, CharField, DecimalField, ManyToManyField, ForeignKeyField, Check
from decimal import Decimal

database = SqliteDatabase('betsy_workshop.db', pragmas={"foreign_keys": 1})
# When using sqlite pragma should be put on foreign_keys (only)


class BaseModel(Model):
    class Meta:
        database = database


class User(BaseModel):
    user_id = IntegerField(unique=True, primary_key=True)
    name = CharField()
    street = CharField()
    town = CharField()


"""
  the user model specifies its fields (or columns) declaratively, 
  I actually think for one seller the product_name should be unique
"""


class Tag(BaseModel):
    tag_id = AutoField(unique=True, primary_key=True)
    name = CharField()


class Product(BaseModel):
    product_id = AutoField(unique=True, primary_key=True)
    product_name = CharField()
    description = CharField()
    price_per_unit = DecimalField(8, 2, True)
    tags = ManyToManyField(Tag)


""" Note : I don't think a manytomany relationship between this table and the table product should be 
           created. A product does have tags but it doesn't have users after all. The table user_products
           has two fields which belong together (product_id and number). This is the reason why a manytomany concept
           is not so easily implementable for that table. 
"""


class Product(BaseModel):
    product_id = AutoField(unique=True, primary_key=True)
    product_name = CharField()
    description = CharField()
    price_per_unit = DecimalField(8, 2, True)
    tags = ManyToManyField(Tag)


class User_product(BaseModel):
    user_id = ForeignKeyField(User)
    product_id = ForeignKeyField(Product)
    number = IntegerField(constraints=[Check('number >=0')])


class Transaction(BaseModel):
    user_id = ForeignKeyField(User)
    product_id = ForeignKeyField(Product)
    number = IntegerField(constraints=[Check('number>0')])
    sell_date = DateField()
    sell_price = DecimalField(8, 2, True)


ProductTag = Product.tags.get_through_model()


def create_tables():
    with database:
        database.create_tables(
            [User, User_product, Product, Transaction, ProductTag, Tag])
