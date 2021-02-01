# Models go here

from peewee import *
from decimal import Decimal

database = SqliteDatabase('betsy_workshop.db', pragmas={
                          "primary_key": True, "foreign_keys": 1})
# Foreign key constraints are incorporated as well as primary_keys to refer to
# such as the product_name and the user_id are considered to be primary keys for
# the tables Product and User and foreign_keys in other tables having these fields


class BaseModel(Model):
    class Meta:
        database = database


class User(BaseModel):
    user_id = IntegerField(unique=True, primary_key=True)
    name = CharField()
    street = CharField()
    town = CharField()

# the user model specifies its fields (or columns) declaratively, like django
# I actually think for one seller the product_name should be unique


class Tags(BaseModel):
    tag_id = AutoField(unique=True, primary_key=True)
    name = CharField()
    # Je zou hier ook met een id kunnen werken. Dan worden de condities net wat
    # anders maar het scheelt niet veel.


class Product(BaseModel):
    product_id = AutoField(unique=True, primary_key=True)
    product_name = CharField()
    description = CharField()
    price_per_unit = DecimalField(8, 2, True)
    number_in_stock = IntegerField(constraints=[Check('number_in_stock>=0')])
    tags = ManyToManyField(Tags)


class User_products(BaseModel):
    user_id = ForeignKeyField(User, backref="User")
    product_id = ForeignKeyField(Product, backref="Product")
    number = IntegerField(constraints=[Check('number >=0')])


class TransactionData(BaseModel):
    user_id = ForeignKeyField(User, backref="User")
    product_id = ForeignKeyField(Product, backref="Product")
    number = IntegerField(constraints=[Check('number>0')])
    sell_date = DateField()
    sell_price = DecimalField(8, 2, True)


class Catalog(BaseModel):
    user_id = ForeignKeyField(User, backref="User")
    product_id = ForeignKeyField(Product, backref="Product")


ProductTag = Product.tags.get_through_model()


def create_tables():
    with database:
        #        database.create_tables([TransactionData, Product, User_products, User])
        database.create_tables(
            [User, User_products, Product, TransactionData, Catalog, ProductTag, Tags])


if __name__ == "__main__":
    create_tables()
