from abc import ABC

from .plan import PlanType
from .person import Instructor

class Exercise(ABC):
    """An abstract class to represent the exercises available on the gym."""

    def __init__(
        self, name: str, date: str, duration: int, capacity: int,
        plan_type: PlanType, active: bool, instructor: Instructor, id=None
    ) -> None:
        super().__init__()
        self._id = id
        self._name: str = name
        
        # TODO: confirm `date` and `duration` types
        self._date = date
        self._duration: int = duration

        self._active: bool = active
        self._capacity: int = capacity
        self._plan_type: PlanType = plan_type
        self._instructor: Instructor = instructor
