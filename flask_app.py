from flask import Flask,render_template,request,session,redirect,url_for
from flask_session import Session
from datetime import date, timedelta, datetime
import sqlite3
from cs50 import SQL

#configure app
app = Flask(__name__)

#configure session
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

DETAILS = {"manager@assignhub.io":"12345678"}
ack = "" #acknoweledgement Message 

# Connect to or create a new SQLite database (e.g., mydb.db)
conn = sqlite3.connect('data.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table (e.g., 'mytable') with some sample columns
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    emp_id INTEGER PRIMARY KEY AUTOINCREMENT,
    emp_name TEXT,
    domain TEXT,
    no_of_tasks INTEGER
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    task_id INTEGER PRIMARY KEY AUTOINCREMENT,
    task_name TEXT,
    description TEXT,
    domain TEXT,
    deadline DATE,
  	emp_id INTEGER,
  	date_assigned DATE
);
''')

# Commit the changes and close the database connection
conn.commit()
conn.close()


db = SQL("sqlite:///data.db")

@app.route("/")
def index():
	return redirect("/manager")


#admin routes
@app.route("/login", methods=["GET","POST"])
def login():
		if request.method == "POST":
				session["Username"] = request.form.get("username_form")
				session["Password"] = request.form.get("password_form")
				global ack
				ack = ""
				return redirect("/manager")
		return render_template("login.html")


@app.route("/manager")
def manager():
    un = session.get("Username")
    pw = session.get("Password")
    if un in DETAILS and DETAILS[un] == pw:
        today = datetime.now()
        dates_and_days = []
        for i in range(7):
            current_date = today + timedelta(days=i)
            day_of_week = current_date.strftime('%A')
            dates_and_days.append((current_date.strftime('%Y-%m-%d'), day_of_week))

        emps = db.execute("SELECT emp_id, emp_name, domain FROM employees")
        for emp in emps:
            dates = db.execute("SELECT task_name, date_assigned FROM tasks WHERE emp_id=?", emp["emp_id"])
            emp["dates"] = {}
            for date in dates:
                emp["dates"][date["task_name"]] = date["date_assigned"]

       	caldata = []
       	for emp in emps:
       		ls = [emp["emp_name"], emp["domain"]]
       		for i in range(7):
       			for tn, dt in emp["dates"].items():
       				if dates_and_days[i][0] == dt:
       					ls.append(tn)
       					break
       			else:
       				ls.append("--")
       		caldata.append(ls)

        return render_template("dashboard.html", username=session.get("Username"), dates=dates_and_days, caldata=caldata, ack=ack)
    else:
        return redirect("/login")


@app.route("/logout")
def logout():
	session["Username"] = None
	session["Password"] = None
	return redirect("/login")


@app.route("/add_emp",methods=["POST"])
def add_emp():
	e_name = request.form.get("e_name")
	e_domain = request.form.get("e_domain")
	if e_name and e_domain:
		db.execute("INSERT INTO employees(emp_name,domain,no_of_tasks) VALUES(?,?,0)",e_name,e_domain)
	return redirect("/")


@app.route("/assign",methods=["POST"])
def assign():
	f_task_name = request.form.get("f_task_name")
	f_description= request.form.get("f_description")
	f_deadline = request.form.get("f_deadline")
	f_domain = request.form.get("f_domain")
	global ack
	ack = ""
	emps = db.execute("SELECT * FROM employees WHERE domain = ? ORDER BY no_of_tasks",f_domain)
	curr_date = date.today()
	date_obj = datetime.strptime(f_deadline, "%Y-%m-%d").date()
	while curr_date <= date_obj:
		for emp in emps:
			busy = db.execute("SELECT * FROM tasks WHERE emp_id = ? AND date_assigned= ? ",emp["emp_id"],str(curr_date))
			if not busy:
				db.execute("INSERT INTO tasks(task_name,description,deadline,domain,emp_id,date_assigned) VALUES(?, ?, ?, ?,?,?)",f_task_name,f_description,f_deadline,f_domain,emp["emp_id"],curr_date)
				db.execute("UPDATE employees SET no_of_tasks = no_of_tasks + 1 WHERE emp_id = ?",emp["emp_id"])
				ack = f"Assigned to {emp['emp_name']} on {curr_date}"
				break
		else:
			curr_date += timedelta(days=1)
			continue
		break
	if not ack:
		ack = "There are no suitable employee."
	print(ack)
	return redirect("/manager")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)
