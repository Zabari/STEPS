from flask import Flask,render_template

app = Flask(__name__)

@app.route("/status")
@app.route("/home")
@app.route("/")
def status():
    return render_template("status.html");

@app.route("/about")
def about():
    return render_template("about.html");

@app.route("/api")
def api():
    return render_template("api.html");

@app.route("/stats")
def stats():
    return render_template("stats.html");

@app.route("/contact")
def contact():
    return render_template("contact.html");

@app.route("/base")
def base():
    return render_template("base.html");


if __name__=="__main__":
    app.debug=True
    app.run()
