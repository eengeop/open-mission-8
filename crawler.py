import yfinance as yf

def get_top_volume_stocks(limit=10):
    # 사용자가 설정한 Fixed Stock List
    tickers = [
        "AAPL", "MSFT", "GOOGL", "AMZN", "TSLA",
        "NVDA", "META", "NFLX", "AMD", "INTC",
        "CSCO", "ORCL", "QCOM"
    ]

    results = []

    for t in tickers:
        stock = yf.Ticker(t)
        info = stock.info

        results.append({
            "ticker": t,
            "price": info.get("regularMarketPrice", 0),
            "volume": info.get("volume", 0)
        })

    return sorted(results, key=lambda x: x["volume"], reverse=True)[:limit]
