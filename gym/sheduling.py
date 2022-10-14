from abc import ABC

from .person import Member
from .exercise import Exercise

class Scheduling:
    """Represents when a member tries to schedule any type of exercise."""

    def __init__(self, member: Member, exercise: Exercise, id=None) -> None:
        self._id = id
        self._member: Member = member
        self._exercise: Exercise = exercise
