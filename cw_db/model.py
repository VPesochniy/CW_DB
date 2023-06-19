from sqlalchemy import String, ForeignKey, Float, Integer, DateTime, Table, Column, Time, Date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from typing import List, Optional
from datetime import date, time, datetime
import config


class Base(DeclarativeBase):
    pass


class Address(Base):
    __tablename__ = "address"

    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement="auto", unique=True, nullable=False, index=True)

    name: Mapped[str] = mapped_column(String, nullable=False)
    address: Mapped[str] = mapped_column(String, nullable=False)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customer.id"))

    customer: Mapped["Customer"] = relationship(back_populates="address")

    def __repr__(self) -> str:
        return f"""id={self.id!r},
        name={self.name!r},
        address={self.address!r},
        customer_id={self.customer_id!r}\n"""

    def __init__(self, input_name: str, input_address: str, input_customer_id: int):
        self.name = input_name
        self.address = input_address
        self.customer_id = input_customer_id


class Courier(Base):
    __tablename__ = "courier"

    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement="auto", unique=True, nullable=False, index=True)

    login: Mapped[str] = mapped_column(String, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    full_name: Mapped[str] = mapped_column(String, nullable=False)
    status: Mapped[str] = mapped_column(String, nullable=False)

    order: Mapped[List["Order"]] = relationship(
        back_populates="courier", cascade="all, delete-orphan")
    schedule: Mapped[List["Schedule"]] = relationship(
        back_populates="courier", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"""id={self.id!r},
        login={self.login!r},
        password={self.password!r},
        full_name={self.full_name!r},
        status={self.status!r}\n"""

    def __init__(self, input_login, input_password: str, input_full_name: str, input_status: str):
        self.login = input_login
        self.password = input_password
        self. full_name = input_full_name
        self.status = input_status


class Customer(Base):
    __tablename__ = "customer"

    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement="auto", unique=True, nullable=False, index=True)

    full_name: Mapped[str] = mapped_column(String, nullable=False)
    phone_number: Mapped[str] = mapped_column(String, nullable=False)

    address: Mapped[List["Address"]] = relationship(
        back_populates="customer", cascade="all, delete-orphan")
    order: Mapped[List["Order"]] = relationship(
        back_populates="customer", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"""id={self.id!r},
        full_name={self.full_name!r},
        phone_number={self.phone_number!r}\n"""

    def __init__(self, input_full_name: str, input_phone_number: str):
        self.full_name = input_full_name
        self.phone_number = input_phone_number


class Item(Base):
    __tablename__ = "item"

    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement="auto", unique=True, nullable=False, index=True)

    name: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[Optional[str]]

    def __repr__(self) -> str:
        return f"""id={self.id!r},
        name={self.name!r},
        price={self.price!r},
        quantity={self.quantity!r},
        description={self.description!r}\n"""

    def __init__(self, input_name: str, input_price: float, input_quantity: int, input_description: Optional[str]):
        self.name = input_name
        self.price = input_price
        self.quantity = input_quantity
        self.description = input_description


class Order(Base):
    __tablename__ = "order"

    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement="auto", unique=True, nullable=False, index=True)

    date_of_creation: Mapped[DateTime] = mapped_column(
        DateTime, nullable=False)
    date_of_completion: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    items_quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    discount: Mapped[Optional[float]]
    cost: Mapped[float] = mapped_column(Float, nullable=False)
    status: Mapped[str] = mapped_column(String, nullable=False)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customer.id"))
    courier_id: Mapped[int] = mapped_column(ForeignKey("courier.id"))

    courier: Mapped["Courier"] = relationship(back_populates="order")
    customer: Mapped["Customer"] = relationship(back_populates="order")

    def __repr__(self) -> str:
        return f"""id={self.id!r}, 
        date_of_creation={datetime.strftime(self.date_of_creation, config.DATETIME_FORMAT)!r}, 
        date_of_completion={datetime.strftime(self.date_of_completion, config.DATETIME_FORMAT) if self.date_of_completion != None else None!r}, 
        quantity={self.items_quantity!r},
        discount={self.discount!r},
        cost={self.cost!r},
        status={self.status!r},
        courier_id={self.courier_id!r},
        customer_id={self.customer_id!r}\n"""

    def __init__(self, input_date_of_creation: datetime, input_date_of_completion: Optional[datetime], input_items_quantity: int, input_discount: Optional[float], input_cost: float, input_status: str, input_courier_id: int, input_customer_id: int):
        self.date_of_creation = input_date_of_creation
        self.date_of_completion = input_date_of_completion
        self.items_quantity = input_items_quantity
        self.discount = input_discount
        self.cost = input_cost
        self.status = input_status
        self.courier_id = input_courier_id
        self.customer_id = input_customer_id


Order_has_Item = Table(
    "order_has_item",
    Base.metadata,
    Column("order_id", ForeignKey("order.id"), primary_key=True),
    Column("item_id", ForeignKey("item.id"), primary_key=True),
)


class Schedule(Base):
    __tablename__ = "schedule"

    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement="auto", unique=True, nullable=False, index=True)

    start_of_shift: Mapped[Time] = mapped_column(
        Time, nullable=False)
    end_of_shift: Mapped[Optional[Time]] = mapped_column(Time)
    date: Mapped[Date] = mapped_column(Date, nullable=False)
    description: Mapped[Optional[str]]
    courier_id: Mapped[int] = mapped_column(ForeignKey("courier.id"))

    courier: Mapped["Courier"] = relationship(back_populates="schedule")

    def __repr__(self) -> str:
        return f"""id={self.id!r}, 
        start_of_shift={time.strftime(self.start_of_shift, config.TIME_FORMAT)!r}, 
        end_of_shift={time.strftime(self.end_of_shift, config.TIME_FORMAT) if self.end_of_shift != None else None!r}, 
        date={date.strftime(self.date, config.DATE_FORMAT)!r},
        description={self.description!r},
        courier_id={self.courier_id!r}\n"""

    def __init__(self, input_start_of_shift: time, input_end_of_shift: Optional[time], input_date: date, input_description: Optional[str], input_courier_id: int):
        self.start_of_shift = input_start_of_shift
        self.end_of_shift = input_end_of_shift
        self.date = input_date
        self.description = input_description
        self.courier_id = input_courier_id


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement="auto", unique=True, nullable=False, index=True)

    login: Mapped[str] = mapped_column(String, nullable=False)
    password: Mapped[str] = mapped_column(String, nullable=False)
    access_level: Mapped[str] = mapped_column(String, nullable=False)

    def __repr__(self) -> str:
        return f"""id={self.id!r},
        login={self.login!r},
        password={self.password!r},
        access_level={self.access_level!r}\n"""

    def __init__(self, input_login: str, input_password: str, input_access_level: str):
        self.login = input_login
        self.password = input_password
        self.access_level = input_access_level
