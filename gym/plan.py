from abc import ABC

from .plan import Plan

class Plan(ABC):
    """An abstract class to represent a gym plan."""

    def __init__(self, plan: Plan, id=None) -> None:
        super().__init__()
        self._id = id
        self._plan: Plan = plan
        