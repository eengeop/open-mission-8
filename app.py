import time
from crawler import get_top_volume_stocks

def print_top_volume_stocks():
    print("\n==============================")
    print("📊 거래량 상위 10 종목")
    print("==============================")

    stocks = get_top_volume_stocks()

    for s in stocks:
        print(f"{s['ticker']}:  가격 {s['price']} USD | 거래량 {s['volume']}")

    print("==============================\n")


if __name__ == "__main__":
    while True:
        print_top_volume_stocks()
        time.sleep(5)
