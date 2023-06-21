import sqlalchemy.orm as orm
import hashlib
import datetime

import model
import config


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
