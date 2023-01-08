from program.db.connection import getCursorInsert, getCursor, getCursorDict

def userAdd(_data):
    _query = f"""INSERT INTO users.user_sign({','.join(_data.keys())}) VALUES('{"','".join(_data.values())}');"""
    with getCursorInsert() as _curr:
        _curr.execute(_query)

def userCheck(_data):
    _query = f"""SELECT count(*) FROM users.user_sign WHERE username = '{_data['username']}' AND password = '{_data['password']}'"""
    print(_query)
    with getCursorDict() as _curr:
        _curr.execute(_query)
        _data = _curr.fetchone()
    return _data['count']