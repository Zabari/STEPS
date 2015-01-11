from flask import Flask,render_template,request
import json, requests

app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():        
    return render_template("test.html");

@app.route("/data", methods = ['POST']) 
def getData():
    if request.method == 'POST':
        r = json.loads(request.data)
        print r
    return "recieved";

if __name__=="__main__":
    app.debug=True
    app.run(host="0.0.0.0",port=8000)
