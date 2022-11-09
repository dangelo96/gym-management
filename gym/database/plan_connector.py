from gym.plan import PlanType
from .utils import run_sql, INVALID_ID

def add(plan_type: PlanType) -> int:
    """
    Adds a plan into the database.

    Parameters
    ----------
        plan: PlanType
            The plan about to be added.

    Returns
    -------
        int
            The id from the added plan.
    """
    added_id: int = INVALID_ID
    
    statement: str = "INSERT INTO WEBUSER.PLANS (PLAN) VALUES (%s) RETURNING *;"
    values: list = [plan_type.plan]
    
    result_set: list = run_sql(statement, values)

    if len(result_set) > 0:
        added_plan_type: tuple = result_set[0]
        added_id = added_plan_type["id"]
    
    return added_id

def delete_by_id(id: int) -> None:
    """
    Given an id, deletes the related plan type.

    Parameters
    ----------
        id: int
            The id from the plan type about to be deleted.

    Returns
    -------
        None
    """
    statement: str = "DELETE FROM WEBUSER.PLANS WHERE id = %s;"
    values: list = [id]

    run_sql(statement, values)

def get_all() -> list:
    """
    Returns all available plans.

    Parameters
    ----------
        None.
    
    Returns
    -------
        list
            A list of each possible Plan saved into the database.
    """
    plans: list = []
    statement: str = "SELECT * FROM WEBUSER.PLANS;"

    result_set: list = run_sql(statement)

    for row in result_set:
        plan_type = PlanType(
            plan=row["plan"],
            id=row["id"]
        )
        plans.append(plan_type)
    
    return plans

def get_by_id(id: int) -> PlanType:
    """
    Given an id, returns the related plan type (if available).

    Parameters
    ----------
        id: int
            The required plan type identifier.

    Returns
    -------
        PlanType
            If present, will return the plan type that matches with the given id.
            If not, will return an empty PlanType (where id is None).
    """
    plan_type: PlanType = PlanType()

    statement: str = "SELECT * FROM WEBUSER.PLANS WHERE ID = %s;"
    values: list = [id]

    result_set: list = run_sql(statement, values)
    
    if len(result_set) > 0:
        returned_plan_type: tuple = result_set[0]
        plan_type = PlanType(
            plan=returned_plan_type["plan"],
            id=returned_plan_type["id"]
        )
    
    return plan_type

def update(plan_type: PlanType) -> None:
    """
    Given an updated Plan Type, inserts its new features into the database.

    Parameters
    ---------
        plan_type: PlanType
            An already updated PlanType, about to be updated inside the DB.

    Returns
    -------
        None
    """
    statement: str = "UPDATE WEBUSER.PLANS SET (PLAN) = %s WHERE ID = %s;"
    values: list = [plan_type.plan, plan_type.id]

    run_sql(statement, values)
