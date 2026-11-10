from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")
def home():
    print("HOME FUNCTION EXECUTED")
    return render_template("index.html")


@app.route("/about")
def hello():
    print("ABOUT FUNCTION EXECUTED")
    return "About page"

if __name__=="__main__":
    app.run(debug=True)