from flask import Flask,render_template

app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():
    return render_template("test.html");

@app.route("/status")
def status():
    return render_template("status.html");


@app.route("/bootstatus")
def bootstatus():
    return render_template("bootstatus.html");

if __name__=="__main__":
    app.debug=True
    app.run()
