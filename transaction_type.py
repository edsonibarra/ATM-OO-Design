from enum import Enum


class TransactionType(Enum):
    BALANCE_INQUIRY = 1,
    DEPOSIT_CASH = 2,
    DEPOSIT_CHECK = 3,
    WITHDRAW = 4,
    TRANSFER = 5


class TransactionStatus(Enum):
    SUCCESS = 1,
    FAILURE = 2,
    BLOCKED = 3,
    FULL = 4,
    PARTIAL = 5,
    NONE = 6


class CustumerStatus(Enum):
    ACTIVE = 1,
    BLOCKED = 2,
    BANNED = 3,
    COMPROMISED = 4,
    ARCHIVED = 5,
    CLOSED = 6,
    UNKOWN = 7
    