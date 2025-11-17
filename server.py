from flask import Flask, render_template, request, jsonify
from crawler import get_stocks
from database import SessionLocal
from models import Favorite

app = Flask(__name__)

default_refresh_interval = 5

@app.route("/", methods = ["GET", "POST"])
def index():
    global default_refresh_interval
    db = SessionLocal()

    if request.method == "POST":
        default_refresh_interval = int(request.form["interval"])

    favorites = db.query(Favorite).all()
    favorite_tickers = [f.ticker for f in favorites]

    db.close()

    return render_template("index.html", interval = default_refresh_interval, favorite_tickers = favorite_tickers)

@app.route("/api/stocks")
def api_stocks():
    stocks = get_stocks()
    return jsonify(stocks)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
