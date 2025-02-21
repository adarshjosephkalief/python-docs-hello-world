from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "PWN3D by SMUDGE ^^"
