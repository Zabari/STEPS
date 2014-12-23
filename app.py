from flask import Flask,render_template

app = Flask(__name__)

@app.route("/home")
@app.route("/") 
def home():
    upOn = "static/img/UpOn.png"
    upOff = "static/img/UpOff.png"
    downOn = "static/img/DownOn.png"
    downOff = "static/img/DownOff.png"
    return render_template("test.html",upOn=upOn,upOff=upOff,downOn=downOn,downOff=downOff);

if __name__=="__main__":
    app.debug=True
    app.run() 
