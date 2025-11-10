import time
from crawler import get_stocks

def choose_interval():
    while True:
        user_input = input("새로고침 간격을 입력하세요: ")

        if user_input.isdigit() and int(user_input)>0:
            return int(user_input)
        print("양의 정수를 입력해주세요.\n")

def print_top_volume_stocks(data):
    print("\n")
    print("=" * 75)
    print("거래량 상위 10 종목")
    print("=" * 75)
    print(f"{'Ticker':<10} {'Company':<30} {'Price($)':<15} {'Volume':<15}")
    print("-" * 75)



    for s in data:
        print(f"{s['ticker']:<10} {s['company_name']:<30} {s['price']:<15} {s['volume']:<15}")

    print("=" * 75)
    print("\n")


if __name__ == "__main__":
    user_interval = choose_interval()

    while True:
        stocks = get_stocks()
        print_top_volume_stocks(stocks)
        time.sleep(user_interval)
