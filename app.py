import time
from crawler import get_top_volume_stocks

def choose_interval():
    while True:
        user_input = input("새로고침 간격을 입력하세요: ")

        if user_input.isdigit() and int(user_input)>0:
            return int(user_input)
        print("양의 정수를 입력해주세요.\n")

def print_top_volume_stocks():
    print("\n==============================")
    print("📊 거래량 상위 10 종목")
    print("==============================")

    stocks = get_top_volume_stocks()

    for s in stocks:
        print(f"{s['ticker']}:  가격 {s['price']} USD | 거래량 {s['volume']}")

    print("==============================\n")


if __name__ == "__main__":
    user_interval = choose_interval()

    while True:
        print_top_volume_stocks()
        time.sleep(user_interval)
