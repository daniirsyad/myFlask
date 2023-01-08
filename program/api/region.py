from program.db.connection import getCursorDict

def getProvince():
    with getCursorDict() as _curr:
        _curr.execute("SELECT prov_id, prov_name FROM data_reg.provinces")
        _data = _curr.fetchall()
    return _data

def getCity(_provId):
    _data = ''
    with getCursorDict() as _curr:
        _curr.execute(f"SELECT city_id, city_name FROM data_reg.cities WHERE prov_id = {_provId}")
        _data = _curr.fetchall()
    return _data

def getDistrict(_cityId):
    with getCursorDict() as _curr:
        _curr.execute(f"SELECT dis_id, dis_name FROM data_reg.districts WHERE city_id = {_cityId}")
        _data = _curr.fetchall()
    return _data

def getSubDistrict(_disId):
    with getCursorDict() as _curr:
        _curr.execute(f"SELECT subdis_id, subdis_name FROM data_reg.subdistricts WHERE dis_id = {_disId}")
        _data = _curr.fetchall()
    return _data