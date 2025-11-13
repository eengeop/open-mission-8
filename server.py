from flask import Flask, render_template, request
from crawler import get_stocks

app = Flask(__name__)

default_refresh_interval = 5

@app.route("/", methods = ["GET", "POST"])
def index():
    global default_refresh_interval

    if request.method == "POST":
        default_refresh_interval = int(request.form["interval"])

    stocks = get_stocks()

    return render_template("index.html", stocks=stocks, interval = default_refresh_interval)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
