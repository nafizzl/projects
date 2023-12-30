from flask import Flask, render_template, url_for

pf = Flask(__name__)

@pf.route('/links')
def links():
    return render_template('profile.html')

@pf.route('/')
def type():
    return render_template('homepage.html')

if __name__ == '__main__':
    pf.run(debug=True)