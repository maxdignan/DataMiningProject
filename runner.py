from exchanges.bitfinex import Bitfinex
from exchanges.bitstamp import Bitstamp
from exchanges.coinapult import Coinapult

import time
import csv

import sys

FILENAME = "btc_prices_evening_1_19_19.csv"
FILENAME = sys.argv[1]

print(FILENAME)

with open(FILENAME, "a") as f:
    writer = csv.writer(f)
    writer.writerow(["epoch", "bitfinex", "bitstamp", "coinapult"])

while True:
	time.sleep(5)
	with open(FILENAME, "a") as f:
		writer = csv.writer(f)
		writer.writerow([int(time.time()), Bitfinex().get_current_price(), Bitstamp().get_current_price(), Coinapult().get_current_price()])
