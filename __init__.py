from flask import Flask,render_template
from flask.ext import restful
from utils import apiHelper

#See here: https://flask-restful.readthedocs.org/en/0.3.1/quickstart.html

app = Flask(__name__)
api = restful.Api(app)
  
######## API Resources ######### 
def fourohfour():
    abort(404, message="Something went wrong.")

class API(restful.Resource):
    def get(self):
        return {'hello': 'world'};


# class getStatus(restful.Resource):
#     def get(self):
#         return apiHelper.getAll()

api.add_resource(API,
                 '/api/test',
                 '/api/getAll')


######## Routes #########
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


######## Run & Debug #########

if __name__=="__main__":
    app.debug=True
    app.run()
