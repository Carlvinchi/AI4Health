from flask import Flask, redirect, url_for, render_template,request
import predictor

app = Flask(__name__)

@app.route('/home',methods=["POST","GET"])
def home():
    if request.method == "POST":
        mdel_name = request.form["model_name"]
        sym1 = request.form["sym1"]
        sym2 = request.form["sym2"]
        sym3 = request.form["sym3"]
        sym4 = request.form["sym4"]
        sym5 = request.form["sym5"]
        sym6 = request.form["sym6"]
        result =predictor.tester(mdel_name,sym1,sym2,sym3,sym4,sym5,sym6)
        param = [mdel_name,result]
        return render_template("user.html", params = param)
    else:
        return render_template("home.html")

@app.route("/<params>")
def user(params):
    return render_template("user.html",params)

if __name__ == "__main__":
    app.run(debug=True)