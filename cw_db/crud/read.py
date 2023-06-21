import sqlalchemy.orm as orm

import model


def read_from_table(db_session: orm.Session, choice: model.Base):
    print("\nREAD\n")
    objects = db_session.query(choice).all()
    for o in objects:
        print(o)
    input()
