from flask import Flask
import pandas as pd
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/<number>")
def convert(number):
    return "The binary number is: " + str(bin(number).replace("0b", "")) + ".\n" + "The hex number is: " + str(hex(number).replace("0x", ""))

if __name__ == "__main__":
    app.run(host='0.0.0.0',port = 5000)