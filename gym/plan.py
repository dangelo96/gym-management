from typing import Optional

class PlanType:
    """A class to represent a gym plan."""

    def __init__(self, 
        id: Optional[int] = None,
        plan: Optional[str] = None
    ) -> None:
        self._id: int = id
        self._plan: str = plan

    @property
    def id(self) -> int:
        return self._id

    @id.setter
    def id(self, _id: int) -> None:
        self._id = _id

    @property
    def plan(self) -> str:
        return self.plan
    
    @plan.setter
    def plan(self, _plan: str) -> None:
        self._plan = _plan