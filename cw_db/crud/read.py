import sqlalchemy.orm as orm

import model
import typing


def get_all_records_from_table(db_session: orm.Session, choice: model.Base) -> typing.List[model.Base]:
    return db_session.query(choice).all()
