from flask import Flask, render_template, request, jsonify
from crawler import get_stocks

app = Flask(__name__)

default_refresh_interval = 5

@app.route("/", methods = ["GET", "POST"])
def index():
    global default_refresh_interval

    if request.method == "POST":
        default_refresh_interval = int(request.form["interval"])

    return render_template("index.html", interval = default_refresh_interval)

@app.route("/api/stocks")
def api_stocks():
    stocks = get_stocks()
    return jsonify(stocks)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
