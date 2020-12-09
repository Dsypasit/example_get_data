def test():
    return {'message':'hello world'}

def get_anime(name):
    return {'name': name}

def return_all(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")

    rows = cur.fetchall()

    return row