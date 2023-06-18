from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import Session
from model import Base, Address, Courier, Customer, Item, Order, Order_has_Item, Schedule, User


def connect_to_db():
    db_engine = create_engine(
        "mysql+pymysql://root:0000@localhost/DB?charset=utf8mb4", echo=False, future=True)
    Base.metadata.create_all(db_engine)
    return db_engine


def make_session(db_engine: Engine):
    with Session(bind=db_engine, autoflush=False) as db_session:
        order_has_item = db_session.query(User).all()
        for o in order_has_item:
            print(o)
        # users = db_session.query(User).filter(User.access_level == "full")
        # for u in users:
        #     print(f"\nhash_password={u.password}\n")
