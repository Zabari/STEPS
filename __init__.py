from flask import Flask,render_template
import json

'''
Add import statement for Zabari's server code
I'll assume module is called `server` and has methods:
    updateDatabase(Dictionary<String:Dictionary> `data`)
        `data` contains key for every escalator (ie, "up46"),
         value is dictionary of data. "Status" key contains status
         of each escalator, and we can easily add more data fields
         to each escalator.
    fetchData(EscalatorName)
          returns nested dictionary with single key Escalator Name, and then
          "status or whatever.
    fetchAll()
        returns same format as above: Dictionary<String:Dictionary>
        x = { "up46": {"status":"True"}}  x{"up46":}
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
@app.route("/getData")
def getData():
    data = server.fetchAll()
    return json.dumps(data)

if __name__=="__main__":
    app.debug=True
    app.run() 
