import inspect
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import Session
import model
from model import Base, Order_has_Item
from config import Menu
# from sqlalchemy.ext.automap import automap_base


def connect_to_db():
    # model.Base = automap_base()
    db_engine = create_engine(
        "mysql+pymysql://root:0000@localhost/DB?charset=utf8mb4", echo=False, future=True)
    Base.metadata.create_all(db_engine)
    # model.Base.prepare(autoload_with=db_engine)
    return db_engine


def make_session(db_engine: Engine):
    with Session(bind=db_engine, autoflush=False) as db_session:
        while True:
            table_name = dict()
            print("\nMAIN MENU:\n")
            for number, value in enumerate(Base.metadata.tables.keys(), 1):
                table_name[number] = value
                print(number, value)
            # for p in (Menu):
                # print(p.value, ". ", p.name, sep="")
            print(db_session.query(Order_has_Item).first())
            user_input = input("\nINPUT: ")
            if user_input.isdigit():
                choice = int(user_input)
                for key in table_name.keys():
                    if choice == key:
                        # print(table_name[choice])
                        model = print_classes(table_name[choice])
                        rows = db_session.query(model).all()
                        for r in rows:
                            print(r)
                        # print(f"\nchoice: {choice}\n")
                        # Order_has_item = model.Base.classes.order_has_item

                        # print(db_session.query(Order_has_item).first())

                # match choice:
                #     case Menu.CREATE.value:
                #         print("\nCREATE\n")
                #         pass
                #     case Menu.READ.value:
                #         print("\nREAD\n")
                #         tables = dict()
                #         for number, value in enumerate(model.Base.metadata.tables.keys(), 1):
                #             tables[value] = number
                #             print(number, value)
                #         input("\n")
                #     case Menu.UPDATE.value:
                #         print("\nUPDATE\n")
                #         pass
                #     case Menu.DELETE.value:
                #         print("\nDELETE\n")
                #         pass
                #     case Menu.EXIT.value:
                #         exit(0)
                #     case _:
                #         print("Некорректный ввод. Попробуйте снова")
            else:
                print("Некорректный ввод. Попробуйте снова")


def print_classes(choice: str) -> model.Base:
    for name, obj in inspect.getmembers(model):
        if name.lower() == choice:
            # print(obj, name)
            return obj
