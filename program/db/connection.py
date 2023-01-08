import psycopg2
import psycopg2.pool
from psycopg2.extras import RealDictCursor
from contextlib import contextmanager

dbpool = psycopg2.pool.ThreadedConnectionPool(
    minconn=1,
    maxconn=1,
    host = "localhost",
    port = 5432,
    dbname = "postgres",
    user = "postgres",
    password = "qwertyuiop")

@contextmanager
def getCursorDict():
    _conn = dbpool.getconn()
    try:
        with _conn.cursor(cursor_factory=RealDictCursor) as _curr:
            yield _curr
            _conn.commit()
        return {"Success":1}
    except Exception as _err:
        _conn.rollback()
        print(_err)
        return {"Success":0,"Message":_err}
    finally:
        dbpool.putconn(_conn)

@contextmanager
def getCursorInsert():
    _conn = dbpool.getconn()
    try:
        with _conn.cursor() as _curr:
            yield _curr
            _conn.commit()
        return {"Success":1}
    except Exception as _err:
        _conn.rollback()
        print(_err)
        return {"Success":0,"Message":_err}
    finally:
        dbpool.putconn(_conn)
    