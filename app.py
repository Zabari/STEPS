from flask import Flask,render_template

app = Flask(__name__)

@app.route("/status")
@app.route("/home")
@app.route("/")
def status():
    return render_template("status.html", title="STEPS");

@app.route("/base")
def base():
    return render_template("base.html", title="STEPS");


@app.route("/about")
def about():
    return render_template("about.html", title="STEPS");

@app.route("/api")
def api():
    return render_template("api.html", title="STEPS");

@app.route("/contact")
def contact():
    return render_template("contact.html", title="STEPS");

@app.route("/stats")
def stats():
    return render_template("stats.html", title="STEPS");


if __name__=="__main__":
    app.debug=True
    app.run()
