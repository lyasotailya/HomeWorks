import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Book, Shop, Sale, Stock

db = 'postgresql'
user = 'postgres'
password = '28081974'
db_name = 'abstr'

DSN = f'{db}://{user}:{password}@localhost:5432/{db_name}'
engine = sqlalchemy.create_engine(DSN)


create_tables(engine)


Session = sessionmaker(bind=engine)
session = Session()


req = session.query(
    Publisher.name,
    Book.title,
    Shop.name,
    Sale.price,
    Sale.count,
    Sale.date_sale
).all().join(
    Book, Book.id_publisher == Publisher.id
             ).join(
    Stock, Stock.id_book == Book.id
).join(
    Shop, Shop.id == Stock.id_shop
).join(
    Sale, Sale.id_stock == Stock.id
)
print(req)

session.close()


