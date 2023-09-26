from flask import Flask,render_template,request
from db import connectionDb as DB
import inspect,sqlite3


IRSV2 = Flask(__name__)


@IRSV2.route("/")
def root():
    return render_template('root.html',NameDisplay=inspect.currentframe().f_code.co_name)

@IRSV2.route("/home")
def home():
    return render_template('home.html',NameDisplay=inspect.currentframe().f_code.co_name)

@IRSV2.route("/user", methods=['GET', 'POST'])
def user():
        
    return render_template('user.html',NameDisplay=inspect.currentframe().f_code.co_name)

@IRSV2.route("/returnDB", methods=['GET', 'POST'])
def returnDB():
    rem = DB.GetTable(sqlite3.connect('IRSV2.db'),'Users')
    return rem

@IRSV2.route("/addDB", methods=['GET', 'POST'])
def addDB():

    username = request.form['Username']
    password = request.form['Password']

    rem = DB.AddUser(sqlite3.connect('IRSV2.db'),username,password)
    return rem

@IRSV2.route("/removeDB", methods=['GET', 'POST'])
def removeDB():
    pass




if __name__ == "__main__":
    IRSV2.run(debug=True)