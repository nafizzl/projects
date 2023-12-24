from flask import Flask, render_template, url_for

pf = Flask(__name__)

@pf.route('/')
def index():
    return render_template('profile.html')

if __name__ == '__main__':
    pf.run(debug=True)