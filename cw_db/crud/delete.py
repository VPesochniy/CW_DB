import sqlalchemy.orm as orm

import model
import crud.read


def delete_entry_from_table(db_session: orm.Session, choice: model.Base) -> model.Base:
    crud.read.read_from_table(db_session, choice)
    print("\nDELETE\n")
    user_input = input("ENTRY ID TO DELETE: ")
    object_to_delete = db_session.query(
        choice).filter(choice.id == user_input).first()
    return object_to_delete
