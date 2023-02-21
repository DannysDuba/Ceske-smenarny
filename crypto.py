import requests
from bs4 import BeautifulSoup


def binance_server():
    url = "https://www.binance.com/cs/price/bitcoin"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    price_binance = soup.find("div", {"class": "css-12ujz79"}).get_text()
    return price_binance


def coinbase_server():
    url = 'https://api.coinbase.com/v2/prices/BTC-USD/spot'
    response = requests.get(url).json()
    return response


def cryptocom_server():
    url = 'https://crypto.com/price/bitcoin'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    prize_crypto = soup.find("span", "chakra-text css-13hqrwd").get_text().replace("USD", "").replace("$", "  $ ")
    return prize_crypto




def main():
    # while True: nekonečná smyčka
    binance = binance_server()
    coinbase = coinbase_server()
    cryptocom = cryptocom_server()
    coinbase_price = format(float(coinbase['data']['amount']), ',.2f')

    print(f"Cena bitcoinu z burzy Binance je:     {binance}")
    print(f"Cena bitcoinu z burzy Coinbase je:    $ {coinbase_price}")
    print(f"Cena bitcoinu z burzy Crypto.com je:{cryptocom}")

    print(50 * "=")
    print("Srovnání českých směnáren")
    print(50 * "=")


    # time.sleep(5) každých 5 sekund stahuje data


if __name__ == '__main__':
    main()
