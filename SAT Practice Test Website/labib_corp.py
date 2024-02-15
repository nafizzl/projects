from flask import Flask, render_template, request, redirect, url_for, session
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash
import os
import pymysql

# flask app instance
labib_corp = Flask(__name__)                                            

# home page route
@labib_corp.route("/", methods=["GET", "POST"])                                                  
def home():
    return render_template("home.html")

# login page route
@labib_corp.route("/login", methods=["GET", "POST"])
def login():
    # use request 
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        check = c.execute("SELECT * FROM SAT_USERS WHERE USERNAME = %s", (username,), fetch_one=True)
    
        # if the database returns None, the username/password combination is an invalid one
        if check and check_password_hash(check["password"], password):
            session["username"] = username
            return redirect(url_for("user"))
        
        else:
            return redirect(url_for("login"))
    else:
        return render_template("signup.html")
@labib_corp.route("/signup", methods=["GET", "POST"])
def signup():

# @labib_corp.route("/user", methods=["GET", "POST"])

# @labib_corp.route("/problems", methods=["GET", "POST"])

if __name__ == "__main__":   
    try: 
        # load credentials
        load_dotenv()                                                       

        # connect using credentials hidden in .env
        nafiz_company = pymysql.connect(                                    
        host = os.getenv("HOST"),
        user = os.getenv("USERNAME"),
        password = os.getenv("PASSWORD")
    )
        # create executable cursor
        c = nafiz_company.cursor()                                          

        # for checking that table exists
        def table_exists(cursor, table_name):                               
            cursor.execute(f"SHOW TABLES LIKE '{table_name}'")
            return cursor.fetchone() is not None
        
        # make the problems table if it hasn't been done yet, with relevant columns
        if not table_exists(c, "SAT_PROBLEMS"):
            c.execute("CREATE TABLE SAT_PROBLEMS(id INT PRIMARY KEY, PROBLEM BLOB, PROBLEM_TYPE VARCHAR(100), ANSWER_MC VARCHAR(1), ANSWER_WRITE INT, CORRECT_ATTEMPTS INT, TOTAL_ATTEMPTS INT, DIFFICULTY INT)")
        
        # make the users table if it hasn't been done yet, with relevant columns 
        if not table_exists(c, "SAT_USERS"):
            c.execute("CREATE TABLE SAT_USERS(id INT PRIMARY KEY, USERNAME VARCHAR(50), PASSWORD VARCHAR(50), FIRST_NAME VARCHAR(50), LAST_NAME VARCHAR(50))")

        # run Flask app
        labib_corp.run(debug=True)                                          
    
    # except statement for handling errors when trying to connect to the tables
    except pymysql.Error as e:
        print(f"Error connecting to the database: {e}")
    
    # close user's connection to database when exiting application
    finally:
        if nafiz_company:
            nafiz_company.close()