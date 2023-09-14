# app.py

import webbrowser  # Import the webbrowser module

from flask import Flask, render_template, request, redirect, url_for
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        units = int(request.form['units'])
        a = float(request.form['a'])
        d = float(request.form['d'])
        s = float(request.form['s'])
        fc = float(request.form['fc'])
        fyl = float(request.form['fyl'])
        fyt = float(request.form['fyt'])
        ρl = float(request.form['ρl'])
        ρt = float(request.form['ρt'])
        v = float(request.form['v'])

        # Store the user inputs in a text file (optional)
        with open('user_inputs.txt', 'w', encoding='utf-8') as file:
            file.write(f"Units: {units}\n")
            file.write(f"a: {a}\n")
            file.write(f"d: {d}\n")
            file.write(f"s: {s}\n")
            file.write(f"fc: {fc}\n")
            file.write(f"fyl: {fyl}\n")
            file.write(f"fyt: {fyt}\n")
            file.write(f"ρl: {ρl}\n")
            file.write(f"ρt: {ρt}\n")
            file.write(f"v: {v}\n")

        # Run your Python script with the user inputs
        result = subprocess.run(
            ['python', 'my_script.py'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        output = result.stdout

        return render_template('result.html', output=output)

    return render_template('index.html')

if __name__ == '__main__':
    # Open the web browser to the local host address
    webbrowser.open('http://localhost:5000/', new=2)

    # Start the Flask app
    app.run(debug=False)