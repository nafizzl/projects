from flask import Blueprint, render_template, request, redirect, url_for
import pandas as pd

path = Blueprint('routes', __name__)

@path.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        return redirect(url_for('routes.login'))
    else:
        return render_template('index.html', greeted = "to nafizzl's medical database.", homepage = True)

@path.route('/admin')
def admin():
    data = {
        "Name": ["Mark Aguire", "Pat Riley", "Phil Jackson"],
        "Age": [58, 65, 60],
        "ID": [11235, 45947, 43673]
    }
    df = pd.DataFrame(data)
    df_html = df.to_html()
    return render_template('adminDatabase.html', table = df_html)

@path.route('/<username>')
def user(username):
    return render_template('index.html', greeted = username,  homepage = False)

@path.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        if user.lower() == 'admin':
            return redirect(url_for("routes.admin"))
        return redirect(url_for("routes.user", username = user))
    else:
        return render_template('login.html')