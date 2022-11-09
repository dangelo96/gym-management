from typing import Optional

class Exercise:
    """A class to represent the exercises available on the gym."""

    def __init__(self, 
        id: Optional[int] = None,
        name: Optional[str] = None,
        date: Optional[str] = None,
        active: Optional[bool] = None,
        capacity: Optional[int] = None,
        duration: Optional[int] = None,
        plan_type_id: Optional[int] = None,
        instructor_id: Optional[int] = None
    ) -> None:
        self._id: int = id
        self._name: str = name
        self._active: bool = active
        self._capacity: int = capacity
        self._duration: int = duration
        self._plan_type_id: int = plan_type_id
        self._instructor_id: int = instructor_id

        # TODO: confirm `date` type
        self._date = date

    @property
    def id(self) -> int:
        return self._id
    
    @id.setter
    def id(self, _id: int) -> None:
        self._id = _id

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, _name: str) -> None:
        self._name = _name

    @property
    def active(self) -> bool:
        return self._active
    
    @active.setter
    def active(self, _active: bool) -> None:
        self._active = _active

    @property
    def capacity(self) -> int:
        return self._capacity
    
    @capacity.setter
    def capacity(self, _capacity: int) -> None:
        self._capacity = _capacity

    @property
    def duration(self) -> int:
        return self._duration
    
    @duration.setter
    def duration(self, _duration: int) -> None:
        self._duration = _duration

    @property
    def plan_type_id(self) -> int:
        return self._plan_type_id
    
    @plan_type_id.setter
    def plan_type_id(self, _plan_type_id: int) -> None:
        self._plan_type_id = _plan_type_id

    @property
    def instructor_id(self) -> int:
        return self._instructor_id
    
    @instructor_id.setter
    def instructor_id(self, _instructor_id: int) -> None:
        self._instructor_id = _instructor_id
