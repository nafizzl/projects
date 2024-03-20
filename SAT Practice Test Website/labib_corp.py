from flask import Flask, render_template, request, redirect, url_for, session
from dotenv import load_dotenv
import bcrypt
import os
import pymysql
import uuid

# flask app instance
labib_corp = Flask(__name__)                                            
load_dotenv()
labib_corp.secret_key = os.getenv("SECRET_KEY")

# home page route
@labib_corp.route("/", methods=["GET", "POST"])                                                  
def home():
    if request.method == "POST":
        if request.form.get("login"):
            return redirect(url_for("login"))
        if request.form.get("signup"):
            return redirect(url_for("signup"))
    return render_template("home.html")

# login page route
@labib_corp.route("/login", methods=["GET", "POST"])
def login():
    # use request 
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        c.execute("SELECT * FROM sat_users WHERE USERNAME = %s", (username,))
        check = c.fetchone()
    
        # if the database returns None, the username/password combination is an invalid one
        if check and bcrypt.checkpw(password.encode("utf-8"), check[2].encode("utf-8")):
            session["username"] = username
            return redirect(url_for("user", user=session.get("username"))) 
        else:
            return render_template("login.html", fail=True) 
    else:
        return render_template("login.html", fail=False)

# signup page route
@labib_corp.route("/signup", methods=["GET", "POST"])
def signup():
    # use request
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        c.execute("SELECT 1 FROM sat_users WHERE USERNAME = %s", (username,))
        check = c.fetchone()
        # if the database returns None, this new user info can be used

        if check:
            return render_template("signup.html", fail=True)
        else:
            hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
            user_id = str(uuid.uuid4())
            c.execute("INSERT INTO sat_users(id, USERNAME, PASSWORD) VALUES (%s, %s, %s)", (id, username, hashed))
            session["username"] = username
            return redirect(url_for("user"))
    else:
        return render_template("signup.html", fail=False)
    
@labib_corp.route("/user", methods=["GET", "POST"])
def user(): 
    if session.get("username"):
        return render_template("user.html", user=session.get("username"))

    

# @labib_corp.route("/problems", methods=["GET", "POST"])

if __name__ == "__main__":   
    nafiz_company = None
    
    try: 
        # load credentials
        load_dotenv()                                                       

        # connect using credentials hidden in .env
        nafiz_company = pymysql.connect(                                    
        host = os.getenv("HOST"),
        user = os.getenv("USER"),
        password = os.getenv("PASSWORD"),
        database = os.getenv("DATABASE")
    )
        # create executable cursor
        c = nafiz_company.cursor()                                          

        # for checking that table exists
        def table_exists(cursor, table_name):                               
            cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
            return cursor.fetchone() is not None
        
        # make the problems table if it hasn't been done yet, with relevant columns
        if not table_exists(c, "sat_problems"):
            c.execute("CREATE TABLE sat_problems(id VARCHAR(50) PRIMARY KEY, PROBLEM BLOB, PROBLEM_TYPE VARCHAR(100), ANSWER_MC VARCHAR(1), ANSWER_WRITE INT, CORRECT_ATTEMPTS INT, TOTAL_ATTEMPTS INT, DIFFICULTY INT)")
        
        # make the users table if it hasn't been done yet, with relevant columns 
        if not table_exists(c, "sat_users"):
            c.execute("CREATE TABLE sat_users(id VARCHAR(50) PRIMARY KEY, USERNAME VARCHAR(50), PASSWORD VARCHAR(255), FIRST_NAME VARCHAR(50), LAST_NAME VARCHAR(50))")

        # run Flask app
        labib_corp.run(debug=True)                                          
    
    # except statement for handling errors when trying to connect to the tables
    except pymysql.Error as e:
        print(f"Error connecting to the database: {e}")
    
    # close user's connection to database when exiting application
    finally:
        if nafiz_company:
            nafiz_company.close()
        if c:
            c.close()