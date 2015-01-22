from flask import Flask,render_template, request
import json, server, time
from flask.ext import restful
from utils import apiHelper

#See here: https://flask-restful.readthedocs.org/en/0.3.1/quickstart.html

app = Flask(__name__)
api = restful.Api(app)


######## API Resources #########

# /api/escalators/all/current
# /api/escalators/up23/current

# /api/escalators/all/history, same as /api/escalators/all/history?min=0&max=100
# /api/escalators/up23/history

# includes next and previous with different min & max values

# /api/escalators/all/history?min=23&max=25
# /api/escalators/up23/history

class API(restful.Resource):
    def get(self, escalator, type):
        return {'hello': 'world'};


api.add_resource(API,
                 '/api/test',
                 '/api/escalators/<string:escalator>/<string:type>')


###### Error Handlers ######

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404




######## Routes #########
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
    return render_template("stats.html", history = history, active = active, tCurrent = tCurrent, tFirst = tFirst, trackers = trackers, title="STEPS")


# @app.route("/histogram")
# def histogram():
#     active = server.fetchStatusAll()
#     history = server.fetchAllTime()
#
#     tCurrent = time.time()
#     tFirst = tCurrent
#     trackers = []
#
#     for esc in history:
#         trackers.append(len(esc)-1)
#         if len(esc) > 0 and esc[0] < tFirst:
#             tFirst = esc[0]
#     return render_template("histogram.html", history = history, active = active, tCurrent = tCurrent, tFirst = tFirst, trackers = trackers)



######## Run & Debug #########

if __name__=="__main__":
    app.debug=True
    app.run()
