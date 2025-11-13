from flask import Flask, render_template
from crawler import get_stocks

app = Flask(__name__)

@app.route("/")
def index():
    stocks = get_stocks()
    return render_template("index.html", stocks=stocks)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
