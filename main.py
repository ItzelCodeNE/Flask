from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
import inspect,sqlite3,os,threading

IRSV2 = Flask(__name__)



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
    
   
    return None

@IRSV2.route("/addDB", methods=['GET', 'POST'])
def addDB():

    username = request.form['Username']
    password = request.form['Password']
        

    
    return register()

@IRSV2.route("/removeDB", methods=['GET', 'POST'])
def removeDB():
    
    id = request.form['id']

    return home()

@IRSV2.route('/<string:User>')
def User(User):
    return render_template('user.html',user=User)



if __name__ == "__main__":
    IRSV2.run(debug=True)