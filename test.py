from flask import Flask,render_template
import time

#fake data:
active = [True, True, False, True, False, False, False, False, True, False, True, True]
history = [[1421130001.432412,1421135432.332143,1421152341.324532,1421161200.334829,1421160517.935594],
           [1421110000.987654,1421160000.0],
           [1421120000.000000,1421133000.0,1421143000.0,1421154000.0]]

tCurrent = time.time()

tFirst = history[0][0]
trackers = []
for esc in history:
    trackers.append(len(esc)-1)
    if esc[0] < tFirst:
        tFirst = esc[0]

app = Flask(__name__)

@app.route("/histogram")
@app.route("/")
def histogram():
    return render_template("histogram.html", history = history, active = active, tCurrent = tCurrent, tFirst = tFirst, trackers = trackers)

if __name__=="__main__":
    app.debug=True
    app.run() 

