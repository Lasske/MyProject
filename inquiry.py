from db import tables, session_scope


with session_scope() as session:
    query = session.query(tables.CarBody)
    print(query)
