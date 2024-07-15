from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Home')

@app.route("/scanner")
def scanner():
    return render_template('scanner.html', title='Scanner')

@app.route("/diagnostics")
def diagnostics():
    return render_template('diagnostics.html', title='Diagnostics')

@app.route("/password_cracker")
def password_cracker():
    return render_template('password_cracker.html', title='Password Cracker')

@app.route("/social_engineering")
def social_engineering():
    return render_template('social_engineering.html', title='Social Engineering')

if __name__ == '__main__':
    app.run(debug=True)