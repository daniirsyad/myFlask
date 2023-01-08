from flask import Flask, render_template, request
from program.config.config import getMenuList
from program.api import region
from program.api import users

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

@app.route("/signup", methods=["GET","POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    elif request.method == "POST":
        users.userAdd(request.json)
        return {"message":"success"}

@app.route("/getMenu")
def getMenu():
    return getMenuList();

# Region API
@app.route("/API/getProvinces")
def getProv():
    return region.getProvince()

@app.route("/API/getCities/<_provId>")
def getCities(_provId):
    return region.getCity(_provId)

@app.route("/API/getDis/<_cityId>")
def getDis(_cityId):
    return region.getDistrict(_cityId)

@app.route("/API/getSubDis/<_disId>")
def getSubDis(_disId):
    return region.getSubDistrict(_disId)
# End of Region API

if __name__ == '__main__':
    app.run(debug=True)