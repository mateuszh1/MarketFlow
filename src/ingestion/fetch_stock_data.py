import requests
import logging

def fetch_stock_data(ticker):
    logging.info(f"Start downloading data for {ticker}")
    url = "https://www.alphavantage.co/query"

    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": ticker,
        "apikey": "demo"
    }



    response = requests.get(url, params=params)
    logging.info(f"API response status code: {response.status_code}")


    data = response.json()
    quote = data.get("Global Quote")
    if not quote:
        logging.warning(f"No stock data for {ticker}")
        return None
    price = float(quote["05. price"])
    open = float(quote["02. open"])
    high = float(quote["03. high"])
    low = float(quote["04. low"])
    previous_close = float(quote["08. previous close"])
    volume = int(quote["06. volume"])

    clean_data = {

    "Symbol": quote["01. symbol"],
    "Date": quote["07. latest trading day"],
    "Open": open,
    "High": high,
    "Low": low,
    "Price": price,
    "Volume": volume,
    "Previous Close": previous_close,

    }
    logging.info(f"Successfully downloaded data for {ticker}")
    return clean_data
if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s | %(message)s"

    )
    print(fetch_stock_data("IBM"))