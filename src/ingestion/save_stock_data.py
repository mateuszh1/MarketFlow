import psycopg
from fetch_stock_data import fetch_stock_data
from getpass import getpass
import logging

def save_stock_data(stock):
   if stock is None:
      return None
   logging.info("Start INSERT to databse")
   password = getpass("Hasło do postgers: ")
   with psycopg.connect(
      dbname="data_engineering", 
      user="postgres",
      password = password,
      host = "localhost",                  
      port = 5432               
        )as conn:
      
      with conn.cursor() as cur:
         cur.execute(
            """ 
         Insert into stock_prices (
           symbol, trade_date, open_price, high_price,
           low_price, close_price, volume, previous_close
         )
         Values(
          %s, %s, %s, %s,
          %s, %s, %s, %s
         )
         ON CONFLICT (symbol,trade_Date) DO NOTHING
         """,
    (
            stock["Symbol"],
            stock["Date"],
            stock["Open"],
            stock["High"],
            stock["Low"],
            stock["Price"],
            stock["Volume"],
            stock["Previous Close"]

    )
         )
         inserted_rows = cur.rowcount
   if inserted_rows == 1:
      logging.info("New stock record inserted")
   else:
      logging.info("Stock record already exists - skipped")
   logging.info("Database operation completed")
if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s | %(message)s"
    )

    stock_data = fetch_stock_data("IBM")
    save_stock_data(stock_data)