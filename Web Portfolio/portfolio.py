import os
from flask import Flask, render_template, url_for, request, redirect

pf = Flask(__name__)

@pf.route('/links', methods=["GET", "POST"])
def links():
    if request.method == "POST":
        buttonName = request.form.get("pfPage")
        if buttonName == "Home":
            return redirect(url_for("home"))
        elif buttonName == "Links":
            return render_template("links.html") 
        elif buttonName == "Projects":
            return redirect(url_for("projects"))
    return render_template('links.html')

@pf.route('/projects', methods=["GET", "POST"])
def projects():
    if request.method == "POST":
        buttonName = request.form.get("pfPage")
        if buttonName == "Home":
            return redirect(url_for("home"))
        elif buttonName == "Links":
            return redirect(url_for("links"))
        elif buttonName == "Projects":
            return render_template("projects.html") 
    return render_template('projects.html')

@pf.route('/home', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        buttonName = request.form.get("pfPage")
        if buttonName == "Home":
            return render_template("homepage.html")
        elif buttonName == "Links":
            return redirect(url_for("links")) 
        elif buttonName == "Projects":
            return redirect(url_for("projects"))
    return render_template('homepage.html')

@pf.route('/')
def website():
    return redirect(url_for("home"))

if __name__ == '__main__':
    pf.run(debug=True, host="0.0.0.0", port = int(os.environ.get('PORT', 8080)))