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


def get_shops(pub: str):
    req = session.query(
        Publisher,
        Book,
        Stock,
        Shop,
        Sale
    ).select_from(
        Shop
    ).join(
        Stock, Stock.id_book == Book.id
    ).join(
        Book, Book.id == Stock.id_Book
    ).join(
        Sale, Sale.id_stock == Stock.id
    )
    if pub.isdigit():
        data = req.filter(Publisher.name == int(pub)).all()
    else:
        data = req.filter(Publisher.name == pub).all()
    for book, shop, price, date in data:
        print(f"{book: <40} | {shop: <10} | {price: <8} | {date.strftime('%d-%m-%Y')}")


session.close()


if __name__ == '__main__':
    publisher = input("Введите имя или id публициста")
    get_shops(publisher)