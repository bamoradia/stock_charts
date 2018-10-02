import requests
import pandas
import numpy
import matplotlib
import json
from config import config


stock = input('Please enter the stock ticker you wish to see: ')

print(stock)

response = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&outputsize=full&apikey={}}'.format(stock, config['key']))

parsed_response = response.json()

# print(len(parsed_response['Time Series (Daily)']))

