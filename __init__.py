from flask import Flask,render_template
import json, server, time

app = Flask(__name__)

###### Error Handlers ######

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404



######     Routes     ######

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
def histogram():
    active = server.fetchStatusAll()
    history = server.fetchAllTime()

    tCurrent = time.time()
    tFirst = tCurrent
    trackers = []

    for esc in history:
        trackers.append(len(esc)-1)
        if len(esc) > 0 and esc[0] < tFirst:
            tFirst = esc[0]
    return render_template("histogram.html", history = history, active = active, tCurrent = tCurrent, tFirst = tFirst, trackers = trackers)



if __name__=="__main__":
    app.debug=True
    app.run()
