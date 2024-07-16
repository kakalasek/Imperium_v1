from flask import Flask, render_template, url_for, redirect, request
from forms import ApiForm
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = "73eeac3fa1a0ce48f381ca1e6d71f077"

endpoints = [False, False, False, False]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Home')

@app.route("/scanner", methods=['GET', 'POST'])
def scanner():
    form = ApiForm()
    if request.method == 'POST' and form.validate():
        try:
            if requests.get(form.endpoint.data).json()["state"] == "Scanner":
                endpoints[0] = True
            return redirect(url_for("scanner"))
        except:
            return redirect(url_for("scanner"))
    return render_template('scanner.html', title='Scanner', form=form, endpoint_set=endpoints[0])

@app.route("/scan")
def scan():
    if endpoints[0]:
        data = requests.get("http://127.0.0.1:3001/@scan").json()
        return data
    return redirect(url_for("scanner"))

@app.route("/diagnostics", methods=['GET', 'POST'])
def diagnostics():
    form = ApiForm()
    if request.method == 'POST' and form.validate():
        try:
            if requests.get(form.endpoint.data).json()["state"] == "Diagnostics":
                endpoints[1] = True
            return redirect(url_for("diagnostics"))
        except:
            return redirect(url_for("diagnostics"))
    return render_template('diagnostics.html', title='Diagnostics', form=form, endpoint_set=endpoints[1])

@app.route("/password_cracker", methods=['GET', 'POST'])
def password_cracker():
    form = ApiForm()
    if request.method == 'POST' and form.validate():
        try:
            if requests.get(form.endpoint.data).json()["state"] == "Password_cracker":
                endpoints[2] = True
            return redirect(url_for("password_cracker"))
        except:
            return redirect(url_for("password_cracker"))
    return render_template('password_cracker.html', title='Password Cracker', form=form, endpoint_set=endpoints[2])

@app.route("/social_engineering", methods=['GET', 'POST'])
async def social_engineering():
    form = ApiForm()
    if request.method == 'POST' and form.validate():
        try:
            if requests.get(form.endpoint.data).json()["state"] == "Social_engineering":
                endpoints[3] = True 
            return redirect(url_for("social_engineering"))
        except:
            return redirect(url_for("social_engineering"))
    return render_template('social_engineering.html', title='Social Engineering', form=form, endpoint_set=endpoints[3])

if __name__ == '__main__':
    app.run(debug=True)