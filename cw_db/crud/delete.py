import sqlalchemy.orm as orm

import model
import crud.read


def delete_entry_from_table(db_session: orm.Session, choice: model.Base, input_id: int) -> model.Base:
    # crud.read.read_from_table(db_session, choice)
    print("\nDELETE\n")
    # user_input = input("ENTRY ID TO DELETE: ")
    object_to_delete = db_session.query(
        choice).filter(choice.id == input_id).first()
    db_session.delete(object_to_delete)
    db_session.commit()
    
    return object_to_delete
