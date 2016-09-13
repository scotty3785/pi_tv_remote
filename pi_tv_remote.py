from flask import Flask, render_template, request
from os import curdir
import subprocess

# Simple command



app = Flask(__name__)



@app.route("/")
def main():
    templateData = {}
    return render_template('remote.html', **templateData)

@app.route('/send/<button>')
def send_ir_command(button):
    command = ['irsend','SEND_ONCE']
    if button == "KEY_POWER":
        command.append('Samsung2')
    else:
        command.append('Samsung1')
    command.append(button)
    command = " ".join(command)
    templateData = {'button':button}
    subprocess.call(command, shell=True)
    return "{} - OK".format(button)
    


if __name__ == "__main__":
    print(curdir)
    app.run(host='0.0.0.0', port=81, debug=True)
