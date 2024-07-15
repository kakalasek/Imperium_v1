from flask import Flask, render_template
from forms import ApiForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "73eeac3fa1a0ce48f381ca1e6d71f077"

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Home')

@app.route("/scanner")
def scanner():
    form = ApiForm()
    return render_template('scanner.html', title='Scanner', form=form)

@app.route("/diagnostics")
def diagnostics():
    form = ApiForm()
    return render_template('diagnostics.html', title='Diagnostics', form=form)

@app.route("/password_cracker")
def password_cracker():
    form = ApiForm()
    return render_template('password_cracker.html', title='Password Cracker', form=form)

@app.route("/social_engineering")
def social_engineering():
    form = ApiForm()
    return render_template('social_engineering.html', title='Social Engineering', form=form)

if __name__ == '__main__':
    app.run(debug=True)