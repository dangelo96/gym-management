from gym.person import Instructor
from gym.exercise import Exercise
from database.utils import run_sql, INVALID_ID

def add(instructor: Instructor) -> int:
    """
    Adds an instructor into the database.

    Parameters
    ----------
        instructor: Instructor
            The instructor about to be added.

    Returns
    -------
        int
            The id from the added instructor.
    """
    added_id: int = INVALID_ID
    
    statement: str = """
        INSERT INTO WEBUSER.INSTRUCTORS (NAME, SURNAME, BIRTH_DATE, ADDRESS, PHONE)
        VALUES (%s, %s, %s, %s, %s) RETURNING *;
    """
    values: list = [
        instructor.name,
        instructor.surname,
        instructor.birth_date,
        instructor.address,
        instructor.phone
    ]

    result_set: list = run_sql(statement, values)

    if len(result_set) > 0:
        added_instructor: tuple = result_set[0]
        added_id = added_instructor["id"]

    return added_id

def delete_by_id(id: int) -> None:
    """
    Given an id, deletes the related instructor.

    Parameters
    ----------
        id: int
            The id from the instructor about to be deleted.
    
    Returns
    -------
        None
    """
    statement: str = "DELETE FROM WEBUSER.INSTRUCTORS WHERE ID = %s;"
    values: list = [id]

    run_sql(statement, values)

def get_all() -> list:
    """
    Returns all available instructors.

    Parameters
    ----------
        None
    
    Returns
    -------
        list
            A list of each possible instructor saved into the database.
    """
    instructors: list = []
    statement: str = "SELECT * FROM WEBUSER.INSTRUCTORS;"

    result_set: list = run_sql(statement)

    for row in result_set:
        instructor = Instructor(
            id=row["id"],
            name=row["name"],
            phone=row["phone"],
            address=row["address"],
            surname=row["surname"],
            birth_date=row["birth_date"]
        )
        instructors.append(instructor)
    
    return instructors

def get_by_id(id: int) -> Instructor:
    """
    Given an id, returns the related instructor (if available).

    Parameters
    ----------
        id: int
            The required instructor identifier.

    Returns
    -------
        Instructor
            If present, will return the instructor that matches with the given id.
            If not, will return an empty Instructor (where id is None).
    """
    instructor: Instructor = Instructor()

    statement: str = "SELECT * FROM WEBUSER.INSTRUCTORS WHERE ID = %s;"
    values: list = [id]
    
    result_set: list = run_sql(statement, values)

    if len(result_set) > 0:
        returned_instructor: tuple = result_set[0]
        instructor = Instructor(
            id=returned_instructor["id"],
            name=returned_instructor["name"],
            phone=returned_instructor["phone"],
            address=returned_instructor["address"],
            surname=returned_instructor["surname"],
            birth_date=returned_instructor["birth_date"]
        )

    return instructor

def update(instructor: Instructor) -> None:
    """
    Given an updated Instructor, inserts its new features into the database.

    Parameters
    ----------
        instructor: Instructor
            An already updated Instructor, about to be updated inside the DB.
    
    Returns
    -------
        None
    """
    statement: str = """
        UPDATE WEBUSER.INSTRUCTORS
        SET (NAME, SURNAME, BIRTH_DATE, ADDRESS, PHONE) = (%s, %s, %s, %s, %s)
        WHERE ID = %s;
    """
    values: list = [
        instructor.name,
        instructor.surname,
        instructor.birth_date,
        instructor.address,
        instructor.phone,
        instructor.id
    ]

    run_sql(statement, values)

def get_instructor_exercises_by_id(instructor_id: int) -> list:
    """
    Given an instructor id, returns all exercises that this instructor is responsible for.

    Parameters
    ----------
        instructor_id: int
            The id of the related instructor.
    
    Returns
    -------
        list
            A list of possible exercises that are taught by the related instructor.
    """
    exercises: list = []

    statement: str = "SELECT * FROM WEBUSER.EXERCISES WHERE INSTRUCTOR = %s"
    values: list = [instructor_id]

    result_set: list = run_sql(statement, values)

    for row in result_set:
        exercise = Exercise(
            id=row["id"],
            name=row["name"],
            date=row["date"],
            active=row["active"],
            capacity=row["capacity"],
            duration=row["duration"],
            plan_type_id=row["plan_type"],
            instructor_id=row["instructor"]
        )
        exercises.append(exercise)

    return exercises
