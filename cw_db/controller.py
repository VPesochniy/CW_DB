import sqlalchemy as db
import sqlalchemy.orm as orm
import model
import config
import datetime
import hashlib


def connect_to_db():
    db_engine = db.create_engine(
        config.DB_TOKEN, echo=False, future=True)
    model.Base.metadata.create_all(db_engine)
    return db_engine


def create_db_session(db_engine: db.Engine) -> orm.Session:
    with orm.Session(bind=db_engine, autoflush=False) as db_session:

        while True:
            table_name = dict()
            for number, value in enumerate(model.Base.metadata.tables.keys(), 1):
                table_name[number] = value
                print(number, ". ", str(table_name[number]).upper(), sep="")
            print(config.Menu.EXIT.value, ". ", config.Menu.EXIT.name, sep="")
            user_input = input("\nINPUT: ")
            match user_input:
                case config.Table.ADDRESS.value:
                    choice = model.Address
                case config.Table.COURIER.value:
                    choice = model.Courier
                case config.Table.CUSTOMER.value:
                    choice = model.Customer
                case config.Table.ITEM.value:
                    choice = model.Item
                case config.Table.ORDER.value:
                    choice = model.Order
                case config.Table.SCHEDULE.value:
                    choice = model.Schedule
                case config.Table.USER.value:
                    choice = model.User
                case config.Menu.EXIT.value:
                    return db_session
                case _:
                    print("Некорректный ввод. Попробуйте снова")
                    input()
            print("\nMAIN MENU:\n")
            for p in (config.Menu):
                print(p.value, ". ", p.name, sep="")
            user_input = input("\nINPUT: ")
            match user_input:
                case config.Menu.CREATE.value:
                    obj = create_entry_in_table(db_session, choice)
                    db_session.add(obj)
                    db_session.commit()
                case config.Menu.READ.value:
                    read_from_table(db_session, choice)
                case config.Menu.UPDATE.value:
                    update_entry_from_table(db_session, choice)
                    db_session.commit()
                case config.Menu.DELETE.value:
                    obj = delete_entry_from_table(db_session, choice)
                    db_session.delete(obj)
                    db_session.commit()
                case config.Menu.EXIT.value:
                    return db_session
                case _:
                    print("Некорректный ввод. Попробуйте снова")
                    input()


def update_entry_from_table(db_session: orm.Session, choice: model.Base):

    read_from_table(db_session, choice)
    print("\nUPDATE\n")
    user_input = input("ENTRY ID TO UPDATE: ")
    object_to_update = db_session.query(
        choice).filter(choice.id == user_input).first()
    modified_object = create_entry_in_table(db_session, choice)
    modified_object.id = object_to_update.id
    db_session.delete(object_to_update)
    db_session.add(modified_object)


def delete_entry_from_table(db_session: orm.Session, choice: model.Base) -> model.Base:
    read_from_table(db_session, choice)
    print("\nDELETE\n")
    user_input = input("ENTRY ID TO DELETE: ")
    object_to_delete = db_session.query(
        choice).filter(choice.id == user_input).first()
    return object_to_delete


def create_entry_in_table(db_session: orm.Session, choice: model.Base) -> model.Base:
    print("\nCREATE\n")
    # TODO: использовать один класс, вместо нескольких input; сделать проверку ввода и убрать комментарии
    match choice:
        case model.Address:
            input_name = input("INPUT_NAME: ")
            input_address = input("INPUT_ADDRESS:")
            input_customer_id = input("INPUT_CUSTOMER_ID: ")
            created_object = model.Address(
                input_name, input_address, input_customer_id)
        case model.Courier:
            input_login = input("INPUT_LOGIN: ")
            input_password = input("INPUT_PASSWORD: ")
            input_full_name = input("INPUT_FULL_NAME: ")
            input_status = input("INPUT_STATUS: ")
            created_object = model.Courier(input_login, input_password,
                                           input_full_name, input_status)
        case model.Customer:
            input_full_name = input("INPUT_FULL_NAME: ")
            input_phone_number = input("INPUT_PHONE_NUMBER: ")
            created_object = model.Customer(
                input_full_name, input_phone_number)
        case model.Item:
            input_name = input("INPUT_NAME: ")
            input_price = input("INPUT_PRICE: ")
            input_quantity = input("INPUT_QUANTITY: ")
            input_description = input("INPUT_DESCRIPTION: ")
            created_object = model.Item(input_name, input_price,
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
            created_object = model.Order(datetime.datetime.now(), None, input_items_quantity,
                                         input_discount, input_cost, input_status, input_courier_id, input_customer_id)
        case model.Schedule:
            # input_start_of_shift = input("INPUT_START_OF_SHIFT: ")
            # input_end_of_shift = input("INPUT_END_OF_SHIFT: ")
            # input_date = input("INPUT_DATE: ")
            input_description = input("INPUT_DESCRIPTION: ")
            input_courier_id = input("INPUT_COURIER_ID: ")
            created_object = model.Schedule(datetime.datetime.strftime(datetime.datetime.now(), config.TIME_FORMAT), None, datetime.datetime.strftime(
                datetime.datetime.now(), config.DATE_FORMAT), input_description, input_courier_id)
        case model.User:
            input_login = input("INPUT_LOGIN: ")
            input_password = input("INPUT_PASSWORD: ")
            hashed_password = hashlib.sha256(input_password.encode("UTF-8"))
            input_access_level = input("INPUT_ACCESS_LEVEL: ")
            created_object = model.User(
                input_login, hashed_password.hexdigest(), input_access_level)
    input()
    return created_object


def read_from_table(db_session: orm.Session, choice: model.Base):
    print("\nREAD\n")
    objects = db_session.query(choice).all()
    for o in objects:
        print(o)
    input()


def verify_user(db_session: orm.Session, input_login: str, input_password: str):
    user = get_user_from_db(db_session, input_login)

    password_to_verify = hashlib.sha256(input_password.encode("UTF-8"))
    if password_to_verify.hexdigest() == user.password and user.access_level == config.Access_level.FULL.value:
        print("SUCCESS!")
    else:
        print("!")
    print("password_to_verify:")
    print(password_to_verify.hexdigest())
    print(user.password)
    print("password_to_verify with encode")
    print(input_password)
    print(input_password.encode("UTF-8"))


def get_user_from_db(db_session: orm.Session, input_login: str) -> model.Base:
    return db_session.query(model.User).filter(model.User.login == input_login).first()
