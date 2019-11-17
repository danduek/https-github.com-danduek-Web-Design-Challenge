from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def eco():
    return render_template("index.html")

@app.route('/Data')
def Data():
    return render_template("Data.html")

@app.route('/comparisson')
def comparisson():
    return render_template("comparisson.html")



if __name__ == "__main__":
    app.run(debug=True)