from abc import ABC

from .plan import Plan

class Person(ABC):
    """The base class to represent a person in the system."""

    def __init__(self, name: str, phone: str, surname: str, address: str, birth_date: str) -> None:
        super().__init__()
        self._name: str = name
        self._phone: str = phone
        self._surname: str = surname
        self._address: str = address
        self._birth_date: str = birth_date

class Instructor(Person):
    """A person who is part of the gym staff."""

    def __init__(self, name: str, phone: str, surname: str, address: str, birth_date: str, id=None) -> None:
        super().__init__(name, phone, surname, address, birth_date)
        self._id = id

class Member(Person):
    """A person who frequents the gym."""

    def __init__(
        self, name: str, phone: str, surname: str, address: str, birth_date: str, 
        email: str, active: bool, plan_type: Plan, start_date: str, id=None
    ) -> None:
        super().__init__(name, phone, surname, address, birth_date)
        self._id = id
        self._email: str = email
        self._active: str = active
        self._plan_type: str = plan_type
        self._start_date: str = start_date
