from flask import Flask, render_template

shop = Flask(__name__)

@shop.route('/')
def home():
    return render_template("home.html")

if __name__ == "__main__":
    shop.run(debug=True)