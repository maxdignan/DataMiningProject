from exchanges.bitfinex import Bitfinex
Bitfinex.get_current_price
Bitfinex.get_current_price()
Bitfinex().get_current_price()
  File "<stdin>", line 1, in <module>
from exchanges.bitstamp import Bitstamp
Bitstamp().get_current_price()
Bitfinex().get_current_price()
import sqlite3
conn = sqlite3.connect('ex.db')
c = conn.cursor()
c.execute("CREATE TABLE btc (data integer, bitstamp real, bitfinex real, okcoin real, huobi real, coinapult real);")
c.execute("INSERT INTO btc VALUES (1000, 6333.33, 633.33, 43443.4, 43.4, 5);")
c.execute("SELECT * FROM btc;")
c
c.rowcount()
c.rowcount
c.fetchone()
print(c.execute("SELECT * FROM btc;"))
import time
time.time()
time.time() * 10000000
time.time() * 1000000
time.time() * 10000000
while True:
	sleep(5)
	c.execute("INSERT INTO btc VALUES (?, ?, ?, ?, ?, ?);", time.time() * 10000000, Bitstamp.get_current_price(), Bitfinex.get_current_price(), 10,10,10)
c.execute("INSERT INTO btc VALUES (?, ?, ?, ?, ?, ?);", time.time() * 10000000, Bitstamp.get_current_price(), Bitfinex.get_current_price(), 10,10,10)
c.execute("INSERT INTO btc VALUES (?, ?, ?, ?, ?, ?);", time.time() * 10000000, Bitstamp().get_current_price(), Bitfinex().get_current_price(), 10,10,10)
c.execute("INSERT INTO btc VALUES (?, ?, ?, ?, ?, ?);", [time.time() * 10000000, Bitstamp().get_current_price(), Bitfinex().get_current_price(), 10,10,10])
c.execute("INSERT INTO btc VALUES (?, ?, ?, ?, ?, ?);", (time.time() * 10000000, Bitstamp().get_current_price(), Bitfinex().get_current_price(), 10,10,10))
c.executemany("INSERT INTO btc VALUES (?, ?, ?, ?, ?, ?);", [(time.time() * 10000000, Bitstamp().get_current_price(), Bitfinex().get_current_price(), 10,10,10)])
c.executemany("INSERT INTO btc VALUES (?, ?, ?, ?, ?, ?);", [(time.time(), Bitstamp().get_current_price(), Bitfinex().get_current_price(), 10,10,10)])
calendar.timegm()
import calendar
calendar.timegm(time.strptime('Jul 9, 2009 @ 20:02:58 UTC', '%b %d, %Y @ %H:%M:%S UTC'))
calendar.timegm(time.strptime(time, '%b %d, %Y @ %H:%M:%S UTC'))
calendar.timegm(time.strptime(time.now(), '%b %d, %Y @ %H:%M:%S UTC'))
calendar.timegm(time.strptime(time.time(), '%b %d, %Y @ %H:%M:%S UTC'))
calendar.timegm()
calendar.timegm(())
int(time.time())
c.executemany("INSERT INTO btc VALUES (?, ?, ?, ?, ?, ?);", [(int(time.time()), Bitstamp().get_current_price(), Bitfinex().get_current_price(), 10,10,10)])
c.fetchone()
c.fetchall()
while True:
	time.sleep(5)
	print({time: int(time.time()), bitfinex: Bitfinex().get_current_price(), bitstamp: Bitstamp().get_current_price()})
while True:
	time.sleep(5)
	d = dict()
	d["time"] = int(time.time())
	d["bitfinex"] = Bitfinex().get_current_price()
	d["bitstamp"] = Bitstamp().get_current_price()
while True:
	time.sleep(5)
	d = dict()
	d["time"] = int(time.time())
	d["bitfinex"] = Bitfinex().get_current_price()
	d["bitstamp"] = Bitstamp().get_current_price()
	print(d)
from exchanges.okcoin import OKCoin
OKCoin
from exchanges.huobi import Huobi
from exchanges.coinapult import Coinapult
import csv
fields = ["epoch seconds", "bitstamp", "bitfinex", "okcoin", "huobi", "coinapult"]
with open("btc_prices.csv", "a") as f:
	writer = csv.writer(f)
	writer.writerow(fields)
with open("btc_prices.csv", "a") as f:
	writer = csv.writer(f)
	writer.writerow([int(time.time(), Bitfinex().get_current_price(), Bitstamp().get_current_price(), OKCoin().get_current_price(), Huobi().get_current_price(), Coinapult().get_current_price())])
with open("btc_prices.csv", "a") as f:
	writer = csv.writer(f)
	writer.writerow([int(time.time(), Bitfinex().get_current_price(), Bitstamp().get_current_price(), OKCoin().get_current_price(), Huobi().get_current_price(), Coinapult().get_current_price())])
with open("btc_prices.csv", "a") as f:
	writer = csv.writer(f)
	writer.writerow([int(time.time(), Bitfinex().get_current_price(), Bitstamp().get_current_price(), Null, Huobi().get_current_price(), Coinapult().get_current_price())])
with open("btc_prices.csv", "a") as f:
	writer = csv.writer(f)
	writer.writerow([int(time.time(), Bitfinex().get_current_price(), Bitstamp().get_current_price(), 'null', Huobi().get_current_price(), Coinapult().get_current_price())])
with open("btc_prices.csv", "a") as f:
	writer = csv.writer(f)
	writer.writerow([int(time.time(), Bitfinex().get_current_price(), Bitstamp().get_current_price(), 'null', 'null', Coinapult().get_current_price())])
with open("btc_prices.csv", "a") as f:
	writer = csv.writer(f)
	writer.writerow([int(time.time()), Bitfinex().get_current_price(), Bitstamp().get_current_price(), 'null', 'null', Coinapult().get_current_price())])
with open("btc_prices.csv", "a") as f:
	writer = csv.writer(f)
	writer.writerow([int(time.time()), Bitfinex().get_current_price(), Bitstamp().get_current_price(), 'null', 'null', Coinapult().get_current_price()])
with open("btc_prices.csv", "a") as f:
	writer = csv.writer(f)
	while True:
		time.sleep(5)
		writer.writerow([int(time.time()), Bitfinex().get_current_price(), Bitstamp().get_current_price(), 'null', 'null', Coinapult().get_current_price()])
while True:
	time.sleep(5)
	with open("btc_prices.csv", "a") as f:
		writer = csv.writer(f)
		writer.writerow([int(time.time()), Bitfinex().get_current_price(), Bitstamp().get_current_price(), 'null', 'null', Coinapult().get_current_price()])
while True:
	time.sleep(5)
	with open("btc_prices2.csv", "a") as f:
		writer = csv.writer(f)
		writer.writerow([int(time.time()), Bitfinex().get_current_price(), Bitstamp().get_current_price(), 'null', 'null', Coinapult().get_current_price()])
with open("btc_prices2.csv", 'r') as f:
	reader = csv.reader(f)
with open("btc_prices2.csv", 'r') as f:
	reader = csv.reader(f)
	reader.read()
with open("btc_prices2.csv", 'r') as f:
	reader = csv.reader(f)
	print(len(reader))
with open("btc_prices2.csv", 'r') as f:
	reader = csv.reader(f)
	for line in reader:
		print(line)
count = 0
with open("btc_prices2.csv", 'r') as f:
	reader = csv.reader(f)
	for line in reader:
		count += 1
count
1495 * 5
1495 * 5 / 60
%save
save
exit()

