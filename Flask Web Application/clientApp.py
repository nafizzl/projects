from flask import Flask, Blueprint, render_template, request, redirect, url_for, sessions
import json
from flask_pymongo import PyMongo

clientApp = Flask(__name__)
clientApp.config["MONGO_URI"] = "mongodb://localhost:27017/medInfoDB"
mongo = PyMongo(clientApp)

try:
    # Attempt a sample database operation to check the connection
    mongo.db.list_collection_names()
    print("Connected to MongoDB")
except Exception as e:
    print(f"Failed to connect to MongoDB: {e}")

with clientApp.app_context():
    try:
        local = mongo.db
        localName = local.name  # Get the database name

        # Check if the database exists on the local server
        if localName not in local.client.list_database_names():
            # Database doesn't exist on the local server, so create it
    
            print(f"Database '{localName}' does not exist. Creating...")

            # Copy data from included json files
            with open(r"C:\Users\19295\projects\Flask Web Application\medInfoDB.Patients.json", "r") as json_file1:
                data = json.load(json_file1)
                local.Patients.insert_many(data)
            
            print(f"Database '{localName}' created.")
        
        else:
            print("Database already exists.")

    except PyMongo.errors.ServerSelectionTimeoutError:
        # Handle connection errors (e.g., the local server is not reachable)
        print("Failed to connect to the local MongoDB server")

path = Blueprint('routes', __name__)

@path.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        return redirect(url_for('routes.login'))
    else:
        return render_template('welcome.html', greeted = "to nafizzl's medical database.", homepage = True, returnHome = False)

@path.route('/admin', methods = ['GET', 'POST'])
def admin():
    if request.method == "POST":
        if request.form.get('adminAction') == "Add New Group":
            return "Added new group"
        else:
            return "Viewed all users"
    else:
        return render_template('admin.html', actionsPage = True)

# @path.route('/admin')
# def addCollection():
    

@path.route('/<username>', methods = ['POST', 'GET'])
def user(username):
    if request.method == "POST":
        return redirect(url_for('routes.home'))
    return render_template('welcome.html', greeted = username,  homepage = False, returnHome = True)

@path.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        password = request.form['password']
        if user == 'admin' and password == 'admin':
            return redirect(url_for("routes.admin"))
        
        user_data = mongo.db.Patients.find_one({'Username': user})

        if user_data and user_data['Password'] == password:
            return redirect(url_for("routes.user", username=user))
        else:
            print(f"Login failed for username: {user}")
            return render_template('login.html', loginFailed=True)
                
    else:
        return render_template('login.html', loginFailed = False)
                
clientApp.register_blueprint(path)

if (__name__) == '__main__':
    clientApp.run(debug=True)               # run app, refresh whenever changes are made live
