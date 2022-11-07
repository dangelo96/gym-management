import psycopg2
import psycopg2.extras as ext

# Constants
INVALID_ID: int = -1

def run_sql(statement: str, values: list | None) -> list:
    """
    Function to execute a SQL statement, into the database.
    
    Parameters
    ----------
        statement: str
            The string that represents the statement itself.
        values: None (default) or list
            The parameters for the statement. 
            Can be None because a statement could need or not a parameter.
    
    Returns
    _______
        list
            A list of each possible result from the query.
    """
    conn = None
    results: list = []

    try:
        conn = psycopg2.connect("host=localhost port=5432 dbname=dbapp user=postgres password=dsacademy")
        cur = conn.cursor(cursor_factory=ext.DictCursor)
        cur.execute(statement, values)
        conn.commit()
        results = cur.fetchall()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            
    return results
