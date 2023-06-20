import inspect
from sqlalchemy import create_engine, Engine, insert
import sqlalchemy.orm as so
import model
import config
import typing
import datetime


def connect_to_db():
    db_engine = create_engine(
        config.DB_TOKEN, echo=False, future=True)
    model.Base.metadata.create_all(db_engine)
    return db_engine


def make_session(db_engine: Engine):
    with so.Session(bind=db_engine, autoflush=False) as db_session:

        while True:
            table_name = dict()
            choice: model.Base
            for number, value in enumerate(model.Base.metadata.tables.keys(), 1):
                table_name[number] = value
                print(number, ". ", str(table_name[number]).upper(), sep="")
            print(config.Menu.EXIT.value, ". ", config.Menu.EXIT.name, sep="")
            user_input = input("\nINPUT: ")
            match user_input:
                case config.Tables.ADDRESS.value:
                    choice = model.Address
                case config.Tables.COURIER.value:
                    choice = model.Courier
                case config.Tables.CUSTOMER.value:
                    choice = model.Customer
                case config.Tables.ITEM.value:
                    choice = model.Item
                case config.Tables.ORDER.value:
                    choice = model.Order
                case config.Tables.SCHEDULE.value:
                    choice = model.Schedule
                case config.Tables.USER.value:
                    choice = model.User
                case config.Menu.EXIT.value:
                    exit(0)
                case _:
                    print("Некорректный ввод. Попробуйте снова")
                    input()
            print("\nMAIN MENU:\n")
            for p in (config.Menu):
                print(p.value, ". ", p.name, sep="")
            user_input = input("\nINPUT: ")
            match user_input:
                case config.Menu.CREATE.value:
                    create_entry_in_table(db_session, choice)
                case config.Menu.READ.value:
                    read_from_table(db_session, choice)
                case config.Menu.UPDATE.value:
                    print("\nUPDATE\n")
                    pass
                case config.Menu.DELETE.value:
                    delete_entry_from_table(db_session, choice)
                case config.Menu.EXIT.value:
                    exit(0)
                case _:
                    print("Некорректный ввод. Попробуйте снова")
                    input()


def delete_entry_from_table(db_session: so.Session, choice: model.Base):
    read_from_table(db_session, choice)
    print("\nDELETE\n")
    user_input = input("ENTRY ID TO DELETE: ")
    object_to_delete = db_session.query(
        choice).filter(choice.id == user_input).first()
    db_session.delete(object_to_delete)
    db_session.commit()


def create_entry_in_table(db_session: so.Session, choice: model.Base):
    print("\nCREATE\n")
    # TODO: использовать один класс, вместо нескольких input; сделать проверку ввода и убрать комментарии
    match choice:
        case model.Address:
            input_name = input("INPUT_NAME: ")
            input_address = input("INPUT_ADDRESS:")
            input_customer_id = input("INPUT_CUSTOMER_ID: ")
            obj = model.Address(input_name, input_address, input_customer_id)
        case model.Courier:
            input_login = input("INPUT_LOGIN: ")
            input_password = input("INPUT_PASSWORD: ")
            input_full_name = input("INPUT_FULL_NAME: ")
            input_status = input("INPUT_STATUS: ")
            obj = model.Courier(input_login, input_password,
                                input_full_name, input_status)
        case model.Customer:
            input_full_name = input("INPUT_FULL_NAME: ")
            input_phone_number = input("INPUT_PHONE_NUMBER: ")
            obj = model.Customer(input_full_name, input_phone_number)
        case model.Item:
            input_name = input("INPUT_NAME: ")
            input_price = input("INPUT_PRICE: ")
            input_quantity = input("INPUT_QUANTITY: ")
            input_description = input("INPUT_DESCRIPTION: ")
            obj = model.Item(input_name, input_price,
                             input_quantity, input_description)
        case model.Order:
            # input_date_of_creation = input("INPUT_DATE_OF_CREATION: ")
            # input_date_of_completion = input("INPUT_DATE_OF_COMPLETION: ")
            input_items_quantity = input("INPUT_ITEMS_QUANTITY: ")
            input_discount = input("INPUT_DISCOUNT: ")
            input_cost = input("INPUT_COST: ")
            input_status = input("INPUT_STATUS: ")
            input_courier_id = input("INPUT_COURIER_ID: ")
            input_customer_id = input("INPUT_CUSTOMER_ID: ")
            obj = model.Order(datetime.datetime.now(), None, input_items_quantity,
                              input_discount, input_cost, input_status, input_courier_id, input_customer_id)
        case model.Schedule:
            # input_start_of_shift = input("INPUT_START_OF_SHIFT: ")
            # input_end_of_shift = input("INPUT_END_OF_SHIFT: ")
            # input_date = input("INPUT_DATE: ")
            input_description = input("INPUT_DESCRIPTION: ")
            input_courier_id = input("INPUT_COURIER_ID: ")
            obj = model.Schedule(datetime.datetime.strftime(datetime.datetime.now(), config.TIME_FORMAT), None, datetime.datetime.strftime(
                datetime.datetime.now(), config.DATE_FORMAT), input_description, input_courier_id)
        case model.User:
            input_login = input("INPUT_LOGIN: ")
            input_password = input("INPUT_PASSWORD: ")
            input_access_level = input("INPUT_ACCESS_LEVEL: ")
            obj = model.User(input_login, input_password, input_access_level)
    db_session.add(obj)
    db_session.commit()
    input()


def read_from_table(db_session: so.Session, choice: model.Base):
    print("\nREAD\n")
    objects = db_session.query(choice).all()
    for o in objects:
        print(o)
    input()
