from sqlalchemy import create_engine, String
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement="auto", unique=True, nullable=False, index=True)
    login: Mapped[str] = mapped_column(String, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    access_level: Mapped[str] = mapped_column(String, nullable=False)

    def __repr__(self) -> str:
        return f"id={self.id}, login={self.login}, password={self.password}, access_level={self.access_level}"


db_engine = create_engine(
    "mysql+pymysql://root:0000@localhost/mydb?charset=utf8mb4", echo=False)
Base.metadata.create_all(db_engine)

with Session(bind=db_engine, autoflush=False) as db_session:
    users = db_session.query(User).filter(User.access_level=="full")
    for u in users:
        print(f"\nhash_password={u.password}\n")
