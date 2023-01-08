from program.db.connection import getCursorInsert

def userAdd(_data):
    _query = f"""INSERT INTO users.user_sign({','.join(_data.keys())}) VALUES('{"','".join(_data.values())}');"""
    with getCursorInsert() as _curr:
        _curr.execute(_query)