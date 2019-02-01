from exchanges.bitfinex import Bitfinex
from exchanges.bitstamp import Bitstamp
from exchanges.coinapult import Coinapult

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

    action_point_bitstamp_price = float(five_seconds_ago_line_ACTION_POINT[2])

    if predicted_current_bitstamp_price > action_point_bitstamp_price:
        if current_actual_bitstamp > action_point_bitstamp_price:
            #true positive
            true_pos += 1
            greaters_true.append(predicted_current_bitstamp_price - current_actual_bitstamp)
        else:
            #false positive
            false_pos += 1
            greaters_false.append(predicted_current_bitstamp_price - current_actual_bitstamp)

        errors.append(predicted_current_bitstamp_price - current_actual_bitstamp)
        greaters.append(predicted_current_bitstamp_price - current_actual_bitstamp)
        perc_greaters.append(100 * (predicted_current_bitstamp_price - current_actual_bitstamp) / action_point_bitstamp_price)

        top.append(current_actual_bitstamp - action_point_bitstamp_price)
    else:
        if current_actual_bitstamp < action_point_bitstamp_price:
            #true negative
            true_neg += 1
            lessers_true.append(predicted_current_bitstamp_price - current_actual_bitstamp)
        else:
            #false negative
            false_neg += 1
            lessers_false.append(predicted_current_bitstamp_price - current_actual_bitstamp)

        errors.append(predicted_current_bitstamp_price - current_actual_bitstamp)
        lessers.append(predicted_current_bitstamp_price - current_actual_bitstamp)
        perc_lessers.append(100 * (predicted_current_bitstamp_price - current_actual_bitstamp) / action_point_bitstamp_price)

        bottom.append(current_actual_bitstamp - action_point_bitstamp_price)

print("true_pos: " + str(true_pos))
print("false_pos: " + str(false_pos))
print("true_neg: " + str(true_neg))
print("false_neg: " + str(false_neg))

print("greaters: " + str(sum(greaters)))
print(sum(greaters_true))
print(sum(greaters_false))
print("lessers: " + str(sum(lessers)))
print(sum(lessers_true))
print(sum(lessers_false))


print(top)
print(bottom)
print(sum(top))
print(sum(bottom))
