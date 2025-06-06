from os import getenv


MIN_RESERVATION_HOURS = int(getenv("MIN_RESERVATION_HOURS", 1))
MAX_RESERVATION_HOURS = int(getenv("MAX_RESERVATION_HOURS", 3))
DEFAULT_AMOUNT = int(getenv("DEFAULT_AMOUNT",100000))
RESTAURANT_OPENING_HOUR = int(getenv("RESTAURANT_OPENING_HOUR", 10))
RESTAURANT_CLOSING_HOUR = int(getenv("RESTAURANT_CLOSING_HOUR", 23))
