from flask import Flask, render_template, request, jsonify
from crawler import get_stocks
from database import SessionLocal, engine, Base
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

@app.route("/api/favorites")
def api_favorites():
    db = SessionLocal()
    favorites = db.query(Favorite).all()
    db.close()

    return jsonify([{"ticker":f.ticker, "company_name":f.company_name}
                   for f in favorites])

@app.route("/favorite/add", methods=["POST"])
def add_favorite():
    data = request.json
    ticker = data["ticker"]
    company = data["company_name"]

    db = SessionLocal()
    exists = db.query(Favorite).filter_by(ticker=ticker).first()

    if not exists:
        fav = Favorite(ticker=ticker, company_name = company)
        db.add(fav)
        db.commit()

    db.close()
    return jsonify({"status":"added"})

@app.route("/favorite/remove", methods=["POST"])
def remove_favorite():
    data = request.json
    ticker = data["ticker"]

    db = SessionLocal()
    db.query(Favorite).filter_by(ticker=ticker).delete()
    db.commit()
    db.close()
    return jsonify({"status": "removed"})

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    app.run(debug=True, port=5000)
