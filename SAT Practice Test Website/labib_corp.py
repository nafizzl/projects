from flask import Flask, render_template

labib_corp = Flask(__name__)

@labib_corp.route('/')
def home():
    return render_template("home.html")

if __name__ == "__main__":
    labib_corp.run(debug=True)