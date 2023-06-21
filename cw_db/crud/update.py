import sqlalchemy.orm as orm

import model
import crud.read


def update_entry_from_table(db_session: orm.Session, choice: model.Base):
    crud.read.read_from_table(db_session, choice)
    print("\nUPDATE\n")
    user_input = input("ENTRY ID TO UPDATE: ")
    object_to_update = db_session.query(
        choice).filter(choice.id == user_input).first()
    modified_object = crud.create.create_entry_in_table(db_session, choice)
    modified_object.id = object_to_update.id
    db_session.delete(object_to_update)
    db_session.add(modified_object)
