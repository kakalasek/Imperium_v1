from flask import Flask, request
import subprocess

app = Flask(__name__)
app.config['SECRET_KEY'] = "73eeac3fa1a0ce48f381ca1e6d71f077"

@app.route("/@test")
def test():
    return {'state': "Scanner"}

@app.route("/@scan")
def scan():
    data = subprocess.getoutput(f"nmap {request.args.get('range')}")
    return {"data": data}

if __name__ == '__main__':
    app.run(debug=True, port=3001)