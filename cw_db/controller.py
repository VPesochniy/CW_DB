from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import Session
from model import Base, Address, Courier, Customer, Item, Order, Order_has_Item, Schedule, User
from config import Menu


def connect_to_db():
    db_engine = create_engine(
        "mysql+pymysql://root:0000@localhost/DB?charset=utf8mb4", echo=False, future=True)
    Base.metadata.create_all(db_engine)
    return db_engine


def make_session(db_engine: Engine):
    with Session(bind=db_engine, autoflush=False) as db_session:
        while True:
            print("\nMAIN MENU:\n")
            for p in (Menu):
                print(p.value, ". ", p.name, sep="")
            user_input = input("\nINPUT: ")
            if user_input.isdigit():
                choice = int(user_input)
                # print(choice)
                match choice:
                    case Menu.CREATE.value:
                        print("\nCREATE\n")
                        pass
                    case Menu.READ.value:
                        print("\nREAD\n")
                        tables = dict()
                        for number, value in enumerate(Base.metadata.tables.keys(), 1):
                            tables[value] = number
                            print(number, value)
                        input("\n")
                        # print(tables)
                        # user_input = input("\nINPUT: ")
                        # if user_input.isdigit():
                        # choice = int(user_input)

                        # print(*(B  ase.metadata.tables.keys()))
                    case Menu.UPDATE.value:
                        print("\nUPDATE\n")
                        pass
                    case Menu.DELETE.value:
                        print("\nDELETE\n")
                        pass
                    case Menu.EXIT.value:
                        exit(0)
                    case _:
                        print("Некорректный ввод. Попробуйте снова")
            else:
                print("Некорректный ввод. Попробуйте снова")
