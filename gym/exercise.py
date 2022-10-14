from abc import ABC

from .plan import Plan
from .person import Instructor

class Exercise(ABC):
    """An abstract class to represent the exercises available on the gym."""

    def __init__(
        self, name: str, date: str, duration: str, capacity: int,
        plan_type: Plan, active: bool, instructor: Instructor, id=None
    ) -> None:
        super().__init__()
        self._id = id
        self._name: str = name
        
        # TODO: confirm `date` and `duration` types
        self._date = date
        self._duration = duration

        self._active: bool = active
        self._capacity: int = capacity
        self._plan_type: Plan = plan_type
        self._instructor: Instructor = instructor
