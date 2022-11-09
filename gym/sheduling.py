from typing import Optional

from .person import Member
from .exercise import Exercise

class Scheduling:
    """Represents when a member tries to schedule any type of exercise."""

    def __init__(self,
        id: Optional[int] = None,
        member: Optional[Member] = None,
        exercise: Optional[Exercise] = None
    ) -> None:
        self._id: int = id
        self._member: Member = member
        self._exercise: Exercise = exercise
