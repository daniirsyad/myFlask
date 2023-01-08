from psycopg2 import extras
from ..db.connection import getCursorDict

def getMenuList():
    with getCursorDict() as _curr:
        _curr.execute("SELECT menu_name,menu_path FROM config.menu ORDER BY position")
        _data = _curr.fetchall()

    return _data