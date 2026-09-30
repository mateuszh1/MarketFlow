import requests

ticker = "IBM"

url = "https://www.alphavantage.co/query"

params = {
    "function": "GLOBAL_QUOTE",
    "symbol": ticker,
    "apikey": "demo"
}

response = requests.get(url, params=params)
print(response.status_code)


data = response.json()
quote = data["Global Quote"]
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

print(clean_data)