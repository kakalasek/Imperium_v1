from flask import Flask, request
import subprocess
import json
import xmltodict

app = Flask(__name__)
app.config['SECRET_KEY'] = "73eeac3fa1a0ce48f381ca1e6d71f077"

def extractHosts(file):
    with open(file, "r") as json_file:
        data = json.load(json_file)
        out = ''
        for host in data['nmaprun']['host']:
            out += host['address']['@addr']
            out += ' '
        return out

def createJson():
    xml_content = subprocess.getoutput(f"nmap -oX - {request.args.get('range')}")
    data_dict = xmltodict.parse(xml_content)
    json_data = json.dumps(data_dict, indent=4, sort_keys=True)
    with open("json_output.json", "w") as output:
        output.write(json_data)

@app.route("/@test")
def test():
    return {'state': "Scanner"}

@app.route("/@scan")
def scan():
    createJson()
    hosts = extractHosts("json_output.json")
    return {"hosts": hosts}

if __name__ == '__main__':
    app.run(debug=True, port=3001)
