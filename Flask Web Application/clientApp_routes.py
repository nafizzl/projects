from flask import Blueprint, render_template, request, redirect, url_for, sessions
from medInfo import pymongo

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
        if user.lower() == 'admin' and password.lower() == 'admin':
            return redirect(url_for("routes.admin"))
        if pymongo.medInfoDB.Patients.find_one({'username': user.lower(), 'password': password}):
            return redirect(url_for("routes.user", username = user))
        else:
            return render_template('login.html', loginFailed = True)
    else:
        return render_template('login.html', loginFailed = False)
        