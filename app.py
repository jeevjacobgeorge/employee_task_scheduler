from flask import Flask,render_template,request,session,redirect
from flask_session import Session

#configure app
app = Flask(__name__)

#configure session
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

DETAILS = {"manager@mulearn":"karma"}

#database code
import sqlite3
# Connect to or create a new SQLite database (e.g., mydb.db)
conn = sqlite3.connect('database.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table (e.g., 'mytable') with some sample columns
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    emp_id INTEGER PRIMARY KEY,
    emp_name TEXT,
    skills TEXT
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    task_id INTEGER PRIMARY KEY,
    task_name TEXT,
    description TEXT,
    deadline DATE,
    skills TEXT
  	emp_id INTEGER,
  	date_assigned DATE
);
''')

# Commit the changes and close the database connection
conn.commit()
conn.close()

from cs50 import SQL
db = SQL("sqlite:///database.db")

@app.route("/")
def index():
	return redirect("/manager")

#admin routes
@app.route("/login", methods=["GET","POST"])
def login():
		if request.method == "POST":
				session["Username"] = request.form.get("username_form")
				session["Password"] = request.form.get("password_form")
				return redirect("/manager")
		return render_template("login.html")

@app.route("/manager")
def manager():
	un = session.get("Username")
	pw = session.get("Password")
	if un in DETAILS and DETAILS[un] == pw:
		return render_template("dashboard.html",username=session.get("Username"))
	else:
		
		return redirect("/login")

# @app.route("/add_task")
# def add_task():



@app.route("/logout")
def logout():	
	session["Username"] = None
	session["Password"] = None
	return redirect("/login")
