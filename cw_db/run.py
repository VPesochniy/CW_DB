from controller import connect_to_db, make_session

if __name__ == "__main__":
    db_engine = connect_to_db()
    make_session(db_engine)
