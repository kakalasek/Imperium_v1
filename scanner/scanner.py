from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = "73eeac3fa1a0ce48f381ca1e6d71f077"

@app.route("/@test")
def test():
    return {'state': True}

if __name__ == '__main__':
    app.run(debug=True, port=3001)