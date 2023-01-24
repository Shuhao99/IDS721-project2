from flask import Flask
import pandas as pd
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

# def city(name):
#     df = pd.read_csv("worldcities.csv")
#     df = df[df['city_ascii'].str.contains(name, na=False)]
#     if df.empty:
#         return "Not Find Result"
#     else:
#         return (df['city'].values[0] + " is located at (latitude, longitude) " + str(df['lat'].values[0]) + ", " + str(df['lng'].values[0])
#               + ". It is in " + df['country'].values[0] + ". " + df['city'].values[0] + " has the population of "
#               + str(df['population'].values[0]) + ".")
@app.route("/<number>")
def convert(number):
    return "The binary number is: " + str(bin(number).replace("0b", "")) + ".\n" + "The hex number is: " + str(hex(number).replace("0x", ""))

if __name__ == "__main__":
    app.run(host='0.0.0.0',port = 5000)