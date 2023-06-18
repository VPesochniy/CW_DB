from enum import Enum

DATE_FORMAT = "%d.%m.%Y"
TIME_FORMAT = "%H:%M"
DATETIME_FORMAT = "%H:%M - %d.%m.%Y"

class Menu(Enum):
    CREATE = 1
    READ = 2
    UPDATE = 3
    DELETE = 4
    EXIT = 0