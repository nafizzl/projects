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
    return render_template('links.html')

@pf.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        buttonName = request.form.get("pfPage")
        if buttonName == "Home":
            return render_template("homepage.html")
        elif buttonName == "Links":
            return redirect(url_for("links")) 
    return render_template('homepage.html')

if __name__ == '__main__':
    pf.run(debug=True)