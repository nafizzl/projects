from flask import Blueprint, render_template
import pandas as pd

path = Blueprint('routes', __name__)

@path.route('/')
def home():
    return render_template('index.html')

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
    return f"Hello { username }!"