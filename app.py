from flask import Flask, render_template, request, url_for, flash, redirect
import pandas as pd
app = Flask(__name__)

@app.route("/", methods=('GET', 'POST'))
def hello():
    if request.method == 'POST':
        print("post success")
        number_ = request.form['number']
        print(number_)
        return redirect(url_for('convert',number=number_))
    else:
        return render_template('index.html')

@app.route("/try/<number>", methods=('GET', 'POST'))
def convert(number): 
    if request.method == 'POST':
        number = request.form['number']
        return redirect(url_for('convert',number=number))
    else:
        print("redirect success")
        Hex = str(hex(int(number)).replace("0x", ""))
        binary = str(bin(int(number)).replace("0b", ""))
        return render_template('index_check.html', Hex = Hex, Binary = binary)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port = 5000)