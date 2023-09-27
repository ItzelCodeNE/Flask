from flask import Flask,render_template,request
from db import connectionDb
import inspect,sqlite3


IRSV2 = Flask(__name__)
connection = connectionDb(sqlite3.connect('IRSv2.db'))

@IRSV2.route("/")
def root():
    return render_template('root.html',NameDisplay=inspect.currentframe().f_code.co_name)

@IRSV2.route("/home")
def home():
    return render_template('home.html',NameDisplay=inspect.currentframe().f_code.co_name)

@IRSV2.route("/login", methods=['GET', 'POST'])
def login():
        
    return render_template('login.html',NameDisplay=inspect.currentframe().f_code.co_name)

@IRSV2.route("/register", methods=['GET', 'POST'])
def register():
        
    return render_template('register.html',NameDisplay=inspect.currentframe().f_code.co_name)

@IRSV2.route("/returnDB", methods=['GET', 'POST'])
def returnDB():
    rem = connection.GetTable('Users')
    return rem

@IRSV2.route("/addDB", methods=['GET', 'POST'])
def addDB():

    username = request.form['Username']
    password = request.form['Password']

    rem = connection.AddUser(username,password)
    return home()

@IRSV2.route("/removeDB", methods=['GET', 'POST'])
def removeDB():
    
    id = request.form['id']

    rem = connection.RemoveUser(id)

    return home()




if __name__ == "__main__":
    IRSV2.run(debug=True)