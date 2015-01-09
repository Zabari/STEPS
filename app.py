from flask import Flask,render_template
import json, requests
'''
Add import statement for Zabari's server code
I'll assume module is called `server` and has methods:
    updateDatabase(Dictionary<String:Dictionary> `data`)
        `data` contains key for every escalator (ie, "4-6"),
         value is dictionary of data. "Status" key contains status
         of each escalator, and we can easily add more data fields
         to each escalator.
    fetchData()
        returns same format as above: Dictionary<String:Dictionary>
'''

app = Flask(__name__)

@app.route("/home")
@app.route("/") 
def home():
    return render_template("test.html");

# Raspberry PI sends to /newData in JSON form
@app.route("/newData", methods = ["POST"])
def newData():
    if request.method == "POST": # and request.secret == "uniqueSecret123456"
        data = json.loads(request.data)
        server.updateDatabase(data)

# JS gets updates from getData
@app.route("/getData", methods = ["POST"])
def newData():
    if request.method == "POST":
        data = server,fetchData()
        server.updateDatabase(data)

if __name__=="__main__":
    app.debug=True
    app.run() 
