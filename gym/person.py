from abc import ABC
from typing import Optional

from .plan import PlanType

class Person(ABC):
    """The base class to represent a person in the system."""

    def __init__(self, 
    name: Optional[str]=None, 
    phone: Optional[str]=None, 
    address: Optional[str]=None, 
    surname: Optional[str]=None, 
    birth_date: Optional[str]=None
    ) -> None:
        super().__init__()
        self._name: str = name
        self._phone: str = phone
        self._address: str = address
        self._surname: str = surname
        self._birth_date: str = birth_date

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, _name: str) -> None:
        self._name = _name

    @property
    def phone(self) -> str:
        return self._phone
    
    @phone.setter
    def phone(self, _phone: str) -> None:
        self._phone = _phone

    @property
    def address(self) -> str:
        return self._address
    
    @address.setter
    def address(self, _address: str) -> None:
        self._address = _address

    @property
    def surname(self) -> str:
        return self._surname
    
    @surname.setter
    def surname(self, _surname: str) -> None:
        self._surname = _surname

    @property
    def birth_date(self) -> str:
        return self._birth_date
    
    @birth_date.setter
    def birth_date(self, _birth_date: str) -> None:
        self._birth_date = _birth_date

class Instructor(Person):
    """A person who is part of the gym staff."""

    def __init__(self,
    name: Optional[str]=None, 
    phone: Optional[str]=None, 
    address: Optional[str]=None, 
    surname: Optional[str]=None, 
    birth_date: Optional[str]=None,
    id: Optional[int]=None
    ) -> None:
        super().__init__(name, phone, surname, address, birth_date)
        self._id: int = id

    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, _id: int) -> None:
        self._id = _id

class Member(Person):
    """A person who frequents the gym."""

    def __init__(self, 
    name: Optional[str]=None, 
    phone: Optional[str]=None, 
    address: Optional[str]=None, 
    surname: Optional[str]=None, 
    birth_date: Optional[str]=None,
    id: Optional[int]=None,
    email: Optional[str]=None,
    active: Optional[bool]=None,
    start_date: Optional[str]=None,
    plan_type: Optional[PlanType]=None,
    ) -> None:
        super().__init__(name, phone, surname, address, birth_date)
        self._id = id
        self._email: str = email
        self._active: bool = active
        self._start_date: str = start_date
        self._plan_type: PlanType = plan_type

    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, _id: int) -> None:
        self._id = _id

    @property
    def email(self) -> str:
        return self._email
    
    @email.setter
    def email(self, _email: str) -> None:
        self._email = _email

    @property
    def active(self) -> bool:
        return self._active
    
    @active.setter
    def active(self, _active: bool) -> None:
        self._active = _active

    @property
    def start_date(self) -> str:
        return self._start_date
    
    @start_date.setter
    def start_date(self, _start_date: str) -> None:
        self._start_date = _start_date

    @property
    def plan_type(self) -> PlanType:
        return self._plan_type
    
    @plan_type.setter
    def plan_type(self, _plan_type: PlanType) -> None:
        self._plan_type = _plan_type
