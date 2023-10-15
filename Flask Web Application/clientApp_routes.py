from flask import Blueprint

path = Blueprint('routes', __name__)

@path.route('/')
def home():
    return "Hello World!"

@path.route('/admin')
def admin():
    return "Hello Admin!"