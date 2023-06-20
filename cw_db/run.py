import controller
import view

if __name__ == "__main__":
    db_engine = controller.connect_to_db()
    db_session = controller.create_db_session(db_engine)
    view.run_app(db_session)
