import sqlalchemy as db
import sqlalchemy.orm as orm
import model
import config
import datetime
import hashlib
import gui.login_window
import gui.main_window
import typing

import crud.create
import crud.read
import crud.update
import crud.delete

import csv
from tkinter import filedialog

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
                    obj = crud.create.create_entry_in_table(db_session, choice)
                    db_session.add(obj)
                    db_session.commit()
                case config.Menu.READ.value:
                    crud.read.read_from_table(db_session, choice)
                case config.Menu.UPDATE.value:
                    crud.update.update_entry_from_table(db_session, choice)
                    db_session.commit()
                case config.Menu.DELETE.value:
                    obj = crud.delete.delete_entry_from_table(
                        db_session, choice)
                    db_session.delete(obj)
                    db_session.commit()
                case config.Menu.EXIT.value:
                    return db_session
                case _:
                    print("Некорректный ввод. Попробуйте снова")
                    input()


def get_object_from_table(db_session: orm.Session, choice: model.Base) -> typing.List[model.Base]:
    return db_session.query(choice).all()


def verify_user(db_session: orm.Session, input_login: str, input_password: str):
    user = _get_user_from_db(db_session, input_login)
    password_to_verify = hashlib.sha256(input_password.encode("UTF-8"))
    if password_to_verify.hexdigest() == user.password:
        match user.access_level:
            case config.Access.FULL.value:
                print("FULL ACCESS")
                gui.login_window.root.destroy()
                gui.main_window.run_app(db_session)
            case config.Access.ADMIN.value:
                print("ADMIN ACCESS")
            case config.Access.MODERATOR.value:
                print("MODERATOR ACCESS")
            case config.Access.VIEWER.value:
                print("VIEWER ACCESS")


def _get_user_from_db(db_session: orm.Session, input_login: str) -> model.Base:
    return db_session.query(model.User).filter(model.User.login == input_login).first()


def export_table_in_csv(db_session: orm.Session, choice: model.Base):
        file_path = _open_file_explorer()
        print(file_path)
        # found_name = _find_name_in_choice(choice)
        file_to_write = open(f"{file_path}.csv", "w")
        csv_writer = csv.writer(file_to_write)
        records = db_session.query(choice).all()
        for row in records:
            csv_writer.writerow([getattr(row, column.name) for column in choice.__mapper__.columns])


def _find_name_in_choice(choice: model.Base) -> str:
    dot_in_string_name = str(choice).find(".")
    quote_in_string_name = str(choice).find("'", dot_in_string_name)
    grep_name = str(choice)[dot_in_string_name+1:quote_in_string_name]
    return grep_name


def _open_file_explorer() -> str:
    return filedialog.asksaveasfilename()
    