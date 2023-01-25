from flask import Flask
import pandas as pd
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hey, It's Shuhao's server!"

@app.route("/<number>")
def convert(number):
    return "The binary number is: " + str(bin(int(number)).replace("0b", "")) + "." + "The hex number is: " + str(hex(int(number)).replace("0x", "")) + "."

if __name__ == "__main__":
    app.run(host='0.0.0.0',port = 5000)