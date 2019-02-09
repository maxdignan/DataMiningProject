from exchanges.bitfinex import Bitfinex
from exchanges.bitstamp import Bitstamp
from exchanges.coinapult import Coinapult

import matplotlib.pyplot as plt

import time
import csv

import sys

lines = []

FILENAME = "btc_prices_morning_1_17_19.csv"
if len(sys.argv) > 1:
    FILENAME = sys.argv[1]

# with open("btc_prices.csv", "r") as f:
with open(FILENAME, "r") as f:
    reader = csv.reader(f)
    lines = [line for line in reader]

true_pos = 0
false_pos = 0
true_neg = 0
false_neg = 0

errors = []
greaters = []
greaters_true = []
greaters_false = []
lessers = []
lessers_true = []
lessers_false = []

perc_greaters = []
perc_lessers = []

top = []
bottom = []

START_LINE = 3
if len(sys.argv) > 2 and sys.argv[2] == "skip_first_line":
    START_LINE = 4


actual_prices = []
predicted_prices = []
time = []
t = 0

for i in range(START_LINE, len(lines)):
# for i in range(4, len(lines)):
    fifteen_seconds_ago_line = lines[i - 3]
    ten_seconds_ago_line = lines[i - 2]
    five_seconds_ago_line_ACTION_POINT = lines[i - 1]
    present_line  = lines[i]

    current_actual_bitstamp = float(present_line[2])

    ten_seconds_ago_bitfinex = float(ten_seconds_ago_line[1])
    fifteen_seconds_ago_bitfinex = float(ten_seconds_ago_line[1])

    predicted_current_bitstamp_price = 385.242 + (0.566143 * (ten_seconds_ago_bitfinex)) + (0.308626 * (fifteen_seconds_ago_bitfinex))

    action_point_bitstamp_price = float(ten_seconds_ago_line[2])

    actual_prices.append(current_actual_bitstamp)
    predicted_prices.append(predicted_current_bitstamp_price)
    time.append(t)
    t += 5

print(len(actual_prices))
print(len(predicted_prices))
#
# with open('actual_prices_dump.txt', 'w') as f:
#     f.write(str(actual_prices))
#
# with open('predicted_prices_dump.txt', 'w') as f:
#     f.write(str(predicted_prices))

fig, ax = plt.subplots()
ax.plot(time, actual_prices, label="actual")
ax.plot(time, predicted_prices, label="predicted")

ax.set(xlabel='time (s)', ylabel='price',
       title='Predicted and Actual BTC Price')

ax.legend()

fig.savefig("predicted_and_actual_plot.png")

plt.show()


print(predicted_prices)
