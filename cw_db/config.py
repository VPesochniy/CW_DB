import os
from enum import Enum

DATE_FORMAT = "%d.%m.%Y"
TIME_FORMAT = "%H:%M"
DATETIME_FORMAT = "%H:%M - %d.%m.%Y"

DB_TOKEN = os.getenv("DB_URL")


class Menu(Enum):
    CREATE = "1"
    READ = "2"
    UPDATE = "3"
    DELETE = "4"
    EXIT = "q"


class Table(Enum):
    ADDRESS = "1"
    COURIER = "2"
    CUSTOMER = "3"
    ITEM = "4"
    ORDER = "5"
    SCHEDULE = "7"
    USER = "8"

class Access_level(Enum):
    FULL = "full"
    ADMIN = "admin"
    MODERATOR = "moderator"
    VIEWER = "viewer"
