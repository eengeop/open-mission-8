import requests
from bs4 import BeautifulSoup

URL = "https://finance.yahoo.com/markets/stocks/most-active/"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def request_html(url=URL):
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.text

def parse_top_10(html):
    soup = BeautifulSoup(html, 'html.parser')
    rows = soup.select("table tbody tr")[:10]

    if not rows:
        print("[ERROR] Yahoo Finance에서 값을 찾을 수 없습니다.")
        return []

    results = []
    for r in rows:
        cols = r.find_all("td")

        results.append({
            "company_name": cols[1].get_text(strip=True),
            "ticker": cols[0].get_text(strip=True),
            "price": r.find("fin-streamer", {"data-field": "regularMarketPrice"}).get_text(strip=True),
            "volume": cols[6].get_text(strip=True)
        })

    return results

def get_stocks():
    html=request_html()
    return parse_top_10(html)